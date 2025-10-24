//inicializar as threads
/* Dica para compilação:
                         gcc -o test1 testThread.c -lpthread */


#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>
#include <semaphore.h>
#include <fcntl.h>

#define N 5
#define LEFT (i + N -1) % N
#define RIGHT (i + 1) % N
#define THINKING 0
#define HUNGRY 1
#define EATING 2
// typedef int semaphore;
int state[N];
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;//mutex do tipo real
sem_t s[N]; //vetor de semaforos
#define TRUE 1
#define FALSE 0

void *philosopher(void *data);
void take_forks(int i);
void put_forks(int i);
void test(int i);

int main (void){
    pthread_t tids[N];

    for(int i=0; i<N; i++) {

        int *j = malloc(sizeof(int));
        *j = i;
        sem_init(&s[i], 0, 0);
        state[i] = THINKING;
        pthread_create(&tids[i], NULL, philosopher, (void *)j);
    }

    for(int i=0; i<N; i++) {
        pthread_join(tids[i], NULL);
        printf("Thread id %ld returned\n", tids[i]);
    }
    return(1);
}

void *philosopher(void *data) {
    int i;
    i = *((int *) data);
    while (TRUE){
        //think();
        printf("filosofo %d pensando \n", i);
        sleep(1);
        printf("filosofo %d faminto \n", i);
        take_forks(i);
        printf("filosofo %d comendo \n", i);
        //eat();
        sleep(6);
        put_forks(i);
    }
}

void take_forks(int i){
    pthread_mutex_lock(&mutex);
    state[i] = HUNGRY;
    test(i);
    pthread_mutex_unlock(&mutex);
    sem_wait(&s[i]);
}

void put_forks(int i){
    pthread_mutex_lock(&mutex);
    state[i] = THINKING;
    test(LEFT);
    test(RIGHT);
    pthread_mutex_unlock(&mutex);
}

void test(int i){

    if(state[i] == HUNGRY && state[LEFT] != EATING && state[RIGHT] !=EATING){
        state[i]=EATING;
        sem_post(&s[i]);
    }
}


