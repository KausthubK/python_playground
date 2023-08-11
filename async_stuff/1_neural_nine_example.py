"""
Working through the quick start tutorial in the Neural Nine channel on YouTube.
https://www.youtube.com/watch?v=6RbJYN7SoRs&ab_channel=NeuralNine
"""

import asyncio


async def acdb():
    print("A")
    await other_function() # force wait for this to finish
    print("B")


async def acb():
    task = asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(1)
    print("B")


async def acbd():
    task = asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(1)
    print("B")
    await task

async def returns_string_abcd():
    task = asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(1)
    print("B")
    return_value = await task
    print(return_value)
    return return_value


async def other_function():
    print("C")
    await asyncio.sleep(2)
    print("D")
    return "ABCD"

def synchronous_function():
    retval = asyncio.run(returns_string_abcd())
    return retval

if __name__ == "__main__":
    print(synchronous_function())
  