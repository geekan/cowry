#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>


int count = 0;
#define SIG_MAX 30

struct prodcons {
    pthread_mutex_t lock;
    pthread_cond_t sig[SIG_MAX];
	int ref;
};

struct prodcons buffer;
int init(struct prodcons *b)
{
    int i = 0;
    pthread_mutex_init(&b->lock, NULL);
    for (i = 0; i < SIG_MAX; i++) {
        pthread_cond_init(&b->sig[i], NULL);
    }
	b->ref = 0;
}

void put(struct prodcons *b, int data, int sig)
{
    while(1) {
        pthread_mutex_lock(&b->lock);
		b->ref |= (1 << sig);
        pthread_cond_wait(&b->sig[sig], &b->lock);
		b->ref &= ~(1 << sig);
        count++;
		printf("signal: %d data: %d count:%d\n", sig, data, count);
        pthread_mutex_unlock(&b->lock);

		int tmp;
		while( !(tmp = (b->ref & (1 << ((sig + 1) % SIG_MAX)))) )
			printf("while-tmp:%d\n", tmp);
        pthread_cond_signal(&b->sig[(sig + 1) % SIG_MAX]);
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
	int resource[SIG_MAX];
    pthread_t p[SIG_MAX];
    void *retval;
    init(&buffer);

	for (i = 0; i < SIG_MAX; i++) {
		resource[i] = i;
		pthread_create(&p[i], NULL, producer, &resource[i]);
	}

	printf("Starting %d pthreads...\n"
		   "Pthreads would print numbers one by one~\n\n", SIG_MAX);
    while(buffer.ref != ((1 << SIG_MAX) - 1));
    printf("\nSending signal[0] to trigger a start\n");
	sleep(1);
    pthread_cond_signal(&buffer.sig[0]);

	for (i = 0; i < SIG_MAX; i++) {
		pthread_join(p[i], &retval);
	}
    return 0;
}
