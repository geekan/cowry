#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

#define PRINT(STH) printf("%s\n", #STH)
#define STR(STH) #STH
#define DO(STH) \
    printf("%s:%d\n", STR(STH), STH);

int count = 0;
#define SIGNAL_MAX 30

struct product_condition {
    pthread_mutex_t lock;
    pthread_cond_t sig[SIGNAL_MAX];
    int ready;
};

struct product_condition buffer;
int init(struct product_condition *b)
{
    int i = 0;
    pthread_mutex_init(&b->lock, NULL);
    for (i = 0; i < SIGNAL_MAX; i++) {
        pthread_cond_init(&b->sig[i], NULL);
    }
    b->ready = 0;
    return 0;
}

void put(struct product_condition *b, int data, int sig)
{
    while(1) {
        pthread_mutex_lock(&b->lock);
        // Say I'm ready to receive a signal..
        // But not a stable way.
        b->ready |= (1 << sig);
        // Unlock the mutex and wait for the signal.
        // If signaled, reacquire the mutex.
        pthread_cond_wait(&b->sig[sig], &b->lock);

        // b->ready &= ~(1 << sig);
        count++;
        printf("signal: %d data: %d count:%d\n", sig, data, count);

        pthread_mutex_unlock(&b->lock);

        // Tell next pthread to continue put.
        pthread_cond_signal(&b->sig[(sig + 1) % SIGNAL_MAX]);
    }
}

void producer_put(int x)
{
    printf("starting pthread:%d\n", x);
    put(&buffer, x, x);
    return;
}

void *producer(void *data)
{
    int d = *(int *)data;
    producer_put(d);
    return NULL;
}

int main(void)
{
    int i;
    int resource[SIGNAL_MAX];
    pthread_t p[SIGNAL_MAX];
    void *retval;
    init(&buffer);

    printf("Starting %d pthreads...\n"
           "Pthreads would print numbers one by one~\n\n", SIGNAL_MAX);

    sleep(1);
    for (i = 0; i < SIGNAL_MAX; i++) {
        resource[i] = i;
        pthread_create(&p[i], NULL, producer, &resource[i]);
    }

    // Make sure all pthreads are ready.
    while(buffer.ready != ((1 << SIGNAL_MAX) - 1));

    printf("\nPress enter to send signal[0] to trigger a start\n");
    getchar();

    DO(pthread_cond_signal(&buffer.sig[0]));

    for (i = 0; i < SIGNAL_MAX; i++) {
        pthread_join(p[i], &retval);
    }
    return 0;
}
