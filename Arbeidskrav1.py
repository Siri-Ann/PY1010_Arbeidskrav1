#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# Innlevering av oppgave for Arbeidskrav 1
# Fra Siri Ann Lorentzen
# E-post: silor3111@usn.no
# Sist oppdatert 26.09.2025 kl. 18.16

#  Jeg skal først beregne og presentere de årlige totalkostnadene for elbil og for bensinbil og deretter skal jeg beregne årlig kostnadsdifferanse basert på informasjonen gitt i oppgaven. 

# Enhetsberegning ifm. divstofforbruk elbil: (KWh/km * km/år) (kr/kWh) =[kr / år]

# Kostnader i kroner for elbil per år:

# In[4]:


Kjl = 10000  # Kjørelengde elbil [km/år]
ForEL = 5000  #Forsikring elbil [kr/år]
TrFor = (3.38 * 365.24)  # Trafikkforsikringsvgift [kr/år] 
DrEL = (0.2 * 2.0)*10000
BomEL = (0.1 *10000)  #Bomavgift elbil ((kr/km) * (km/år)) = [kr/år)
SumEL = ForEL + TrFor + DrEL + BomEL
print('SumEL =', SumEL)


# Enhetsberegning ifm. divstofforbruk elbil: (KWh/km * km/år) (kr/kWh) (km) =[kr / år]
# 
# Enhetsberegning i forbindelse med trafikkforsikring:
# (kr/dag) (dag/år) = [kr/år]
# 
# Enhetsberegning bomavgift:
# (kr/km)(km/år) = [kr/år]

# Kostnader i kroner for bensinbil per år:

# In[5]:


Kjl = 10000  # Kjørelengde bensinbil [km/år]
ForBE = 7500  # Forsikring bensinbil [kr/år]
TrFor = (3.38 * 365.24)  # Trafikkforsikringsvgift [kr/år] 
DrBE = (1.0 *10000)  # Drivstofforbruk bensinbil [kr/år]
BomBE = (0.3 * 10000)  # Bomavgift bensinbil
SumBE = ForBE + TrFor + DrBE + BomBE
print('SumBE =', SumBE)



# Enhetsberegning i forbindelse med trafikkforsikring: (kr/dag) (dag/år) = [kr/år]
# 
# Enhetsbergning i forbindelse med drivstofforbruk: (kr/km)(km/år) = [kr/år]
# 
# Enhetsberegning bomavgift: (kr/km)(km/år) = [kr/år] 

# Fra bergningen over ser man at bensinbil er dyrere enn bensinbil.
# 
# Årlig kostnadsdifferanse viser hvor mye dyrere i kroner det er å ha bensinbil i forhold til elbil per år:

# In[6]:


Kdiff = SumBE - SumEL  # Årlig kostnadsdifferanse [kr/år]
print('Kdiff =', Kdiff)


# In[ ]:




