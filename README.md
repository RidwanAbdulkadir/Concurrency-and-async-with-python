# Async and Concurrency in Python - Learning Roadmap

## Phase 1: Fundamentals (Week 1-2)

### 1.1 Core Concepts
- **Synchronous vs Asynchronous**: Blocking vs non-blocking execution
- **Concurrency vs Parallelism**: Multiple tasks vs multiple processors
- **Event Loop**: The core of async programming—what it is and how it works
- **Coroutines**: Functions that can pause and resume (async/await syntax)

### 1.2 Key Topics to Cover
- [ ] Understand the Global Interpreter Lock (GIL) in Python
- [ ] Learn `async` and `await` keywords
- [ ] Study coroutines and how they differ from regular functions
- [ ] Understand event loops and how `asyncio.run()` works

### 1.3 Hands-On Practice
- [ ] Run `example1.py` - understand sync vs async timing differences
- [ ] Create simple async functions with `asyncio.sleep()`
- [ ] Use `asyncio.gather()` to run multiple coroutines concurrently
- [ ] Measure execution time differences

---

## Phase 2: AsyncIO Basics (Week 2-3)

### 2.1 Core AsyncIO Tools
- [ ] **asyncio.gather()**: Run multiple coroutines concurrently, wait for all
- [ ] **asyncio.create_task()**: Schedule a coroutine as a task
- [ ] **asyncio.wait()**: Wait for first completion or all completions
- [ ] **asyncio.Queue**: Async-safe queue for inter-task communication
- [ ] **asyncio.Lock/Semaphore**: Synchronization primitives

### 2.2 Common Patterns
- [ ] Producer-Consumer pattern with asyncio.Queue
- [ ] Timeout handling with `asyncio.wait_for()`
- [ ] Exception handling in async code
- [ ] Cancellation with `asyncio.CancelledError`

### 2.3 Practical Projects
- [ ] Fetch multiple URLs concurrently using `aiohttp`
- [ ] Create a simple async echo server with `asyncio`
- [ ] Build an async task queue with retry logic

---

## Phase 3: Threading (Week 3-4)

### 3.1 When to Use Threading
- Threading breaks the GIL for I/O-bound operations
- Good for CPU-bound tasks when combined with multiprocessing
- Use `concurrent.futures.ThreadPoolExecutor`

### 3.2 Core Concepts
- [ ] Thread creation and lifecycle
- [ ] Thread synchronization: Lock, RLock, Condition, Event
- [ ] Thread pools and executors
- [ ] Daemon threads

### 3.3 Hands-On Practice
- [ ] Create threads manually with `threading.Thread()`
- [ ] Use `ThreadPoolExecutor` for parallel I/O operations
- [ ] Implement locks to prevent race conditions
- [ ] Compare performance: async vs threading

---

## Phase 4: Multiprocessing (Week 4-5)

### 4.1 Core Concepts
- [ ] Process creation and the process pool
- [ ] Inter-process communication: Queue, Pipe, Manager
- [ ] Shared state and synchronization across processes
- [ ] When to use multiprocessing vs threading vs async

### 4.2 Common Patterns
- [ ] `multiprocessing.Pool` for parallel computations
- [ ] Process-to-process communication
- [ ] Handling process termination and cleanup
- [ ] Debugging multiprocess applications

### 4.3 Practical Projects
- [ ] CPU-bound task parallelization (data processing, calculations)
- [ ] Worker pool pattern with process pools
- [ ] Inter-process work distribution

---

## Phase 5: Advanced AsyncIO (Week 5-6)

### 5.1 Advanced Patterns
- [ ] Custom event loops
- [ ] Combining async with threading (`loop.run_in_executor()`)
- [ ] Async context managers and decorators
- [ ] Streaming and async generators

### 5.2 Third-Party Libraries
- [ ] **aiohttp**: Async HTTP client/server
- [ ] **aiofiles**: Async file I/O
- [ ] **asyncpg/motor**: Async database drivers
- [ ] **celery**: Distributed task queue

### 5.3 Real-World Applications
- [ ] Build an async web scraper
- [ ] Create async API endpoints with FastAPI
- [ ] Implement real-time WebSocket communication

---

## Phase 6: Performance & Optimization (Week 6-7)

### 6.1 Profiling & Debugging
- [ ] Profile async code with `asyncio.Task`
- [ ] Debug race conditions and deadlocks
- [ ] Monitor event loop performance
- [ ] Tools: `asyncio.debug()`, `cProfile`, `py-spy`

### 6.2 Optimization Techniques
- [ ] Batch operations efficiently
- [ ] Reduce context switching overhead
- [ ] Memory management in long-running tasks
- [ ] Connection pooling for I/O operations

### 6.3 Benchmarking
- [ ] Compare sync vs async vs threading vs multiprocessing
- [ ] Identify bottlenecks in your code
- [ ] Tune pool sizes and batch sizes

---

## Phase 7: Choosing the Right Tool (Week 7-8)

### Decision Tree:
```
Does your task need parallelism?
├─ YES: Is it CPU-bound?
│  ├─ YES → Use multiprocessing (or async with threading fallback)
│  └─ NO → Is it I/O-bound?
│     ├─ YES (network/file I/O) → Use asyncio
│     └─ YES (GIL-bound) → Use threading
└─ NO: Is it I/O-bound?
   ├─ YES → Use asyncio (preferred) or threading
   └─ NO → Synchronous code is fine
```

---

## Learning Resources

### Official Documentation
- [Python asyncio docs](https://docs.python.org/3/library/asyncio.html)
- [threading docs](https://docs.python.org/3/library/threading.html)
- [multiprocessing docs](https://docs.python.org/3/library/multiprocessing.html)

### Key Concepts to Understand
1. **The GIL**: Why threading doesn't parallelize CPU work
2. **Event Loops**: The heart of async programming
3. **Coroutines**: Pauseable, resumeable functions
4. **Executors**: Bridges between async and sync code

### Recommended Projects (In Order)
1. Async HTTP requests (fetch multiple URLs)
2. Threading example (I/O-bound file processing)
3. Multiprocessing example (CPU-bound calculations)
4. Async web server with FastAPI
5. Full-stack: Async API + database + real-time updates

---

## Common Pitfalls to Avoid

- ❌ Using `time.sleep()` in async code (use `await asyncio.sleep()`)
- ❌ Not awaiting coroutines (they won't execute)
- ❌ Mixing blocking code in async tasks
- ❌ Using multiprocessing for I/O-bound tasks
- ❌ Not handling exceptions in concurrent tasks
- ❌ Creating too many threads/processes

---

## Progress Tracking

Track your progress as you work through each phase:

- [ ] Phase 1: Fundamentals
- [ ] Phase 2: AsyncIO Basics
- [ ] Phase 3: Threading
- [ ] Phase 4: Multiprocessing
- [ ] Phase 5: Advanced AsyncIO
- [ ] Phase 6: Performance & Optimization
- [ ] Phase 7: Master the decision tree

Good luck with your learning journey! 🚀
