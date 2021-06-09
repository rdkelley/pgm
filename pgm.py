#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pgmpy.factors.discrete import TabularCPD


# In[3]:


from pgmpy.models import BayesianModel


# In[45]:


model = BayesianModel([
    ("Difficulty", "Grade"), 
    ("Intelligence", "Grade"), 
    ("Grade", "Letter"),
    ("Intelligence", "SAT")
])


# In[46]:


difficulty_cpd = TabularCPD(variable = "Difficulty", variable_card = 2, values = [[.6],[.4]])


# In[47]:


intelligence_cpd = TabularCPD(variable = "Intelligence", variable_card = 2, values = [[.7],[.3]])


# In[48]:


sat_cpd = TabularCPD(variable = "SAT", 
                     variable_card = 2, 
                     evidence = ["Intelligence"], 
                     evidence_card = [2], 
                     values = [[.95, 0.2], [.05, .8]])


# In[49]:


grade_cpd = TabularCPD(variable = "Grade", 
                     variable_card = 3, 
                     evidence = ["Difficulty", "Intelligence"], 
                     evidence_card = [2, 2], 
                     values = [[.3,.05,.9,.5],[.4,.25,.08,.3],[.3,.7,.02,.2]])


# In[50]:


letter_cpd = TabularCPD(variable = "Letter", 
                     variable_card = 2, 
                     evidence = ["Grade"], 
                     evidence_card = [3], 
                     values = [[.1,.4,.99],[.9,.6,.01]])


# In[51]:


model.add_cpds(difficulty_cpd, intelligence_cpd, sat_cpd, grade_cpd, letter_cpd)


# In[52]:


model.get_cpds()


# In[55]:


from pgmpy.inference import VariableElimination


# In[58]:


infer = VariableElimination(model)


# In[60]:


getRecc = infer.query(variables = ["Letter"])
print(getRecc)


# In[67]:


intelg3 = infer.query(variables = ["Intelligence"], evidence = {'Grade': 0})
print(intelg3)


# In[74]:


intelg3sat = infer.query(variables = ["Intelligence"], evidence = {'Grade': 0, 'SAT': 1})
print(intelg3sat)


# In[ ]:




