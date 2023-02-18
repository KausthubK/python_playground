import logging
import os
from datetime import datetime

from colorama import Fore
from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            # this doesn't use record.created, so it is slightly off
            now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_record["timestamp"] = now
        # log_record["severity"] = record.levelname.upper()
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname
        log_record["file_name"] = record.filename
        log_record["line_no"] = record.lineno

    def process_log_record(self, log_record):
        if log_record["level"] == "INFO":
            level = "INFO "
            colour = Fore.GREEN
        if log_record["level"] == "WARNING":
            level = "WARN "
            colour = Fore.YELLOW
        if log_record["level"] == "DEBUG":
            level = log_record["level"]
            colour = Fore.MAGENTA
        if log_record["level"] == "ERROR" or log_record["level"] == "CRITICAL":
            level = log_record["level"]
            colour = Fore.RED
        print(
            f"{log_record['timestamp']} {colour}{level}{Fore.RESET} [{log_record['name']}] {log_record['message']}"
        )
        return log_record


def get_json_logger(name: str = "default-logger-name"):
    json_formatter = CustomJsonFormatter("%(timestamp)s %(level)s %(name)s %(message)s")
    json_handler = logging.StreamHandler()
    json_handler.setFormatter(json_formatter)
    logger = logging.getLogger(name)
    if len(logger.handlers) == 0:
        logger.addHandler(json_handler)
    logger.setLevel(os.environ.get("LOG_LEVEL", "DEBUG"))
    return logger
