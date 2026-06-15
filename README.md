# CodeToAGI — Episode 25 Challenge Solution

## Async Python Challenge

In Episode 25 we learned:

- async def
- await
- asyncio.gather()
- asyncio.Semaphore()
- async context managers
- asyncio.run()

This repository contains the complete solution to the challenge presented in the video.

---

## Challenge

### Step 1

Create an async function:

```python
async def fetch_user(user_id):
```

that simulates a network request and returns a fake user.

### Step 2

Use:

```python
asyncio.gather()
```

to fetch 10 users concurrently.

Measure the total execution time.

### Step 3

Add:

```python
asyncio.Semaphore(3)
```

so that only 3 requests can run at the same time.

Compare the execution time.

### Step 4

Create an async context manager named:

```python
class Timer:
```

using:

```python
__aenter__()
__aexit__()
```

to automatically measure execution time.

### Step 5

Run everything using:

```python
asyncio.run(main())
```

---

## Expected Output

Without a semaphore:

```text
⏱ Elapsed Time: ~1 second
```

With:

```python
Semaphore(3)
```

you should see roughly:

```text
⏱ Elapsed Time: ~4 seconds
```

because only 3 requests can execute concurrently.

---

## Key Lesson

Concurrency is not always about running everything at once.

In real systems we often need to:

- Respect API rate limits
- Protect databases
- Avoid overwhelming servers

A Semaphore gives us controlled concurrency.

```python
sem = asyncio.Semaphore(3)
```

means:

> Never allow more than 3 tasks to run simultaneously.

This is one of the most common patterns in production async applications.

---

## Video

Watch Episode 25 on YouTube:

**Async Python — async/await, asyncio.gather, Tasks, Async Context Managers**

---

## Channel

CodeToAGI

Daily Python → Agentic AI lessons.
