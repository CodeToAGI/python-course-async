"""
CodeToAGI - Episode 25 Challenge Solution

Topics:
- async def
- await
- asyncio.gather
- asyncio.Semaphore
- async context managers
- timing execution

Run:
python challenge_solution.py
"""

import asyncio
import time


class Timer:
    async def __aenter__(self):
        self.start = time.perf_counter()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        elapsed = time.perf_counter() - self.start
        print(f"\n⏱ Elapsed Time: {elapsed:.2f} seconds")


async def fetch_user(user_id: int):
    print(f"Fetching user {user_id}...")
    await asyncio.sleep(1)  # Simulate network request
    return {
        "id": user_id,
        "name": f"User {user_id}"
    }


async def fetch_user_with_limit(user_id: int, semaphore: asyncio.Semaphore):
    async with semaphore:
        return await fetch_user(user_id)


async def fetch_without_limit():
    print("\n=== WITHOUT SEMAPHORE ===")

    async with Timer():
        tasks = [
            fetch_user(user_id)
            for user_id in range(1, 11)
        ]

        users = await asyncio.gather(*tasks)

    print(f"\nFetched {len(users)} users")
    return users


async def fetch_with_limit():
    print("\n=== WITH SEMAPHORE (LIMIT = 3) ===")

    semaphore = asyncio.Semaphore(3)

    async with Timer():
        tasks = [
            fetch_user_with_limit(user_id, semaphore)
            for user_id in range(1, 11)
        ]

        users = await asyncio.gather(*tasks)

    print(f"\nFetched {len(users)} users")
    return users


async def main():
    print("🚀 Async Pipeline Challenge Solution")

    await fetch_without_limit()
    await fetch_with_limit()

    print("\n✅ Challenge Complete")


if __name__ == "__main__":
    asyncio.run(main())
