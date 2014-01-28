
同步机制列表
=====

1. 原子操作(atomic)
2. 信号量(semaphore)
3. 读写信号量(rw_semaphore)
4. 自旋锁(spinlock)
5. 大内核锁(BKL -- Big Kernel Lock)
> 基本被废弃
6. 读写锁(rwlock)
7. 大读者锁(brlock-Big Reader Lock)
8. RCU(Read-Copy Update)
> 使用rcu_read_lock来保证读指针不被改变
> rcu_assign_pointer来进行rcu操作（似乎前提是你要知道哪些东西要rcu保护）
9. 顺序锁(seqlock)

引用
=====
* [Linux 内核的同步机制，第 2 部分](http://www.ibm.com/developerworks/cn/linux/l-synch/part2/)
* [透过 Linux 内核看无锁编程](http://www.ibm.com/developerworks/cn/linux/l-cn-lockfree/)
