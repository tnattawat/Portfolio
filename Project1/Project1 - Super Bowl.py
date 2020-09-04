#!/usr/bin/env python
# coding: utf-8

# # 1. TV, halftime shows, and the Big Game 

# In[2]:


import pandas as pd
super_bowls = pd.read_csv(r'C:\Users\to_so\Dropbox\My PC (LAPTOP-OJ46F5BO)\Desktop\Data Science\Project1\datasets\super_bowls.csv')
tv = pd.read_csv(r'C:\Users\to_so\Dropbox\My PC (LAPTOP-OJ46F5BO)\Desktop\Data Science\Project1\datasets\tv.csv')
halftime_musicians = pd.read_csv(r'C:\Users\to_so\Dropbox\My PC (LAPTOP-OJ46F5BO)\Desktop\Data Science\Project1\datasets\halftime_musicians.csv')

# Display the first five rows of each DataFrame
display(super_bowls.head())
display(tv.head())
display(halftime_musicians.head())


# # 2. Taking note of dataset issues

# In[3]:


# Summary of the TV data to inspect
tv.info()

print('\n')

# Summary of the halftime musician data to inspect
halftime_musicians.info()


# # 3. Combined points distribution

# In[37]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('seaborn')

# Plot a histogram of combined points
plt.hist(super_bowls.combined_pts)
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowl')
plt.show()

# Display the Super Bowls with the highest and lowest combined scores
display(super_bowls[super_bowls.combined_pts > 70])
display(super_bowls[super_bowls.combined_pts < 25])


# # 4. Point difference distribution

# In[34]:


# Plot a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowl')
plt.show()

# Display the closest games and biggest blowouts
display(super_bowls[super_bowls.difference_pts == 1])
display(super_bowls[super_bowls.difference_pts >= 35])


# # 5. Do blowouts translate to lost viewers?

# In[20]:


# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')
display(games_tv)

import seaborn as sns

# Create a scatter plot with a linear regression model fit
sns.regplot(x=games_tv['difference_pts'], y=games_tv['share_household'], data=games_tv)


# # 6. Viewership and the ad industry over time

# In[31]:


# Create a figure with 3x1 subplot
# Activate the top subplot
plt.subplot(3, 1, 1)
plt.plot(tv['super_bowl'], tv['avg_us_viewers'], color='#648FFF')
plt.title('Avergae Number of US Viewers')

# Activate the middle subplot
plt.subplot(3, 1, 2)
plt.plot(tv['super_bowl'], tv['rating_household'], color='#DC267F')
plt.title('Household Rating')

# Activate the bottom subplot
plt.subplot(3, 1, 3)
plt.plot(tv['super_bowl'], tv['ad_cost'], color='#FFB000')
plt.title('Ad Cost')

plt.xlabel('SUPER BOWL')
plt.tight_layout()


# # 7. Halftime shows weren't always this great

# In[33]:


# Display all halftime musicians for Super Bowls up to and including Super Bowl XXVII
halftime_musicians[halftime_musicians.super_bowl <= 27]


# # 8. Who has the most halftime show appearances?

# In[38]:


# Count halftime show appearances for each musician and sort them from most to least
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)

# Display musicians with more than one halftime show appearance
halftime_appearances[halftime_appearances['super_bowl'] > 1]


# 9. Who performed the most songs in a halftime show?

# In[39]:


# Filter out most marching bands
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# Plot a histogram of number of songs per performance
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel('Number of Song Per Halftime Performance')
plt.ylabel('Number of Musicians')
plt.show()

# Sort the non-band musicians by number of songs per appearance...
no_bands = no_bands.sort_values('num_songs', ascending=False)

# Display the top 15 musicians
display(no_bands.head(15))


# # 10. Conclusion

# In[40]:


# 2018-2019 conference champions
patriots = 'New England Patriots'
rams = 'Los Angeles Rams'

# Who will win Super Bowl LIII?
super_bowl_LIII_winner = patriots
print('The winner of Super Bowl LIII will be the', super_bowl_LIII_winner)


# In[ ]:




