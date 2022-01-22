#theory about Genetic Algorithms: https://docs.google.com/document/d/1ZpfnvheWFhLDUtXobiGHjDo6jdNPjanvJrqP6voc5P4/edit#heading=h.x3ja0dy6pkqp


#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import random as rd
from random import randint
import matplotlib.pyplot as plt
import numpy as np


# In[42]:


#creating the dataset
course_n = np.arange(1, 6)
credits_limit = [int(x) for x in input("Enter the maximum amount of credits: ").split(",")]
weight = [int(x) for x in input("Enter the number of credits for each course: ").split(",")]
value = [int(x) for x in input("Enter the importance of these courses for you (ex., from 1 to 10): ").split(",")]

#the created dataset
print('The courses:')
print('Course num.       Importance      Credits')
for i in range(course_n.shape[0]):
    print('{0}                 {1}                {2}\n'.format(course_n[i], value[i], weight[i]))


# In[43]:


#parameters setting
n_of_solutions_pop = 10
size_pop = (n_of_solutions_pop, course_n.shape[0])
print('Population size = {}'.format(size_pop))

pop_init = np.random.randint(2, size = size_pop)
pop_init = pop_init.astype(int)
generat_num = 50
print('Initial population: \n{}'.format(pop_init))


# In[44]:


#fitness function: 
#if the sum of credits (weights) of the chosen courses is less or equal than the maximum number of credits, 
#then fitness = the sum of values of the chosen courses
#otherwise, fitness = 0
def fitness_eval(weight, value, pop, lim):
    fitness = np.empty(pop.shape[0])
    for i in range(pop.shape[0]):
        Sum_1 = np.sum(pop[i] * value)
        Sum_2 = np.sum(pop[i] * weight)
        if Sum_2 <= lim:
            fitness[i] = Sum_1
        else :
            fitness[i] = 0 
    return fitness.astype(int)  


# In[45]:


#selection
def selection(fitness, par_num, pop):
    fitness = list(fitness)
    par = np.empty((par_num, pop.shape[1]))
    for i in range(par_num):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        par[i,:] = pop[max_fitness_idx[0][0], :]
        fitness[max_fitness_idx[0][0]] = -999999
    return par


# In[46]:


#crossover
def crossover(par, child_num):
    child = np.empty((child_num, par.shape[1]))
    crossover_point = int(par.shape[1]/2)
    crossover_rate = 0.8
    i=0
    while (par.shape[0] < child_num):
        parent1_index = i%par.shape[0]
        parent2_index = (i+1)%par.shape[0]
        x = rd.random()
        if x > crossover_rate:
            continue
        parent1_index = i%par.shape[0]
        parent2_index = (i+1)%par.shape[0]
        child[i,0:crossover_point] = par[parent1_index,0:crossover_point]
        child[i,crossover_point:] = par[parent2_index,crossover_point:]
        i=+1
    return child    


# In[47]:


#mutation
def mutation(child):
    muts = np.empty((child.shape))
    mut_rate = 0.4
    for i in range(muts.shape[0]):
        rand = rd.random()
        muts[i,:] = child[i,:]
        if rand > mut_rate:
            continue
        int_random_value = randint(0,child.shape[1]-1)    
        if muts[i,int_random_value] == 0 :
            muts[i,int_random_value] = 1
        else :
            muts[i,int_random_value] = 0
    return muts     


# In[48]:


#optimization
def optimize(weight, value, pop, size_pop, generat_num, lim):
    parameters, fitness_history = [], []
    par_num = int(size_pop[0]/2)
    child_num = size_pop[0] - par_num 
    for i in range(generat_num):
        fitness = fitness_eval(weight, value, pop, lim)
        fitness_history.append(fitness)
        par = selection(fitness, par_num, pop)
        child = crossover(par, child_num)
        muts = mutation(child)
        pop[0:par.shape[0], :] = par
        pop[par.shape[0]:, :] = muts
        
    print('Last generation: \n{}\n'.format([pop])) 
    fitness_last_gen = fitness_eval(weight, value, pop, lim)      
    print('Fitness of the last generation: \n{}\n'.format(fitness_last_gen))
    max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
    parameters.append(pop[max_fitness[0][0],:])
    return parameters, fitness_history


# In[49]:


#implementation
parameters, fitness_history = optimize(weight, value, pop_init, size_pop, generat_num, credits_limit)
print('The optimized parameters: \n{}'.format(parameters))
selected_items = course_n * parameters
print('\nThe courses that maximizes the value and not exceed the max number of credits:')
for i in range(selected_items.shape[1]):
  if selected_items[0][i] != 0:
     print('{}\n'.format(selected_items[0][i]))


# In[58]:


#graphical representation
#fitness_history_mean = [np.mean(fitness) for fitness in fitness_history]fitness_history_max = [np.max(fitness) for fitness in fitness_history]
#plt.plot(list(range(generat_num)), fitness_history_mean, label = 'Mean Fitness')
#plt.plot(list(range(generat_num), fitness_history_max, label = 'Max Fitness')
#plt.legend()
#plt.title('Change of fitness throughout generations')
#plt.xlabel('Generations')
#plt.ylabel('Fitness')
#plt.show()
#print(np.asarray(fitness_history).shape)


# The code is based on (Genetic Algorithm: Part 3 — Knapsack Problem, 2022).
# 
# References:
# Medium. 2022. Genetic Algorithm: Part 3 — Knapsack Problem. [online] Available at: <https://medium.com/koderunners/genetic-algorithm-part-3-knapsack-problem-b59035ddd1d6> [Accessed 20 January 2022].
