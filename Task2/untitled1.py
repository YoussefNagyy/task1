##The percentage of smoking females
smoking_females = df[(df['sex'] == 'female') & (df['smoker'] == 'yes')].shape[0]
total_people = df[df['sex']=='female'].shape[0]
percentage = (smoking_females / total_people) * 100
print(f"The percentage of smoking females is: {percentage:.2f}%")

##The region with the highest average charges
region_charges = df.groupby('region')['charges'].mean()
max_cost_region = region_charges.idxmax()

print(f"The region with the highest average charges is: {max_cost_region}")

# Which gender has the maximum insurance rate?
df[df['charges'] == df['charges'].max()]['sex']

##  what is the average percentage of female smoker age?
df[(df['sex'] == 'female') & (df['smoker'] == 'yes')]['age'].mean()

Males_chid = df[(df['sex'] == 'male') & (df['children'] > 0)].shape[0]
total_people = df[df['sex']=='male'].shape[0]
percentage = (Males_chid/ total_people) * 100
print(f": {percentage:.2f}%")

##  What are the percentage of the females who hase children insurance?
per  = (df[(df['sex'] == 'female') & (df['children'] > 0 )].shape[0] )/(df[(df['sex'] == 'female')].shape[0])*100
print("{:.2f} %".format(per))

##  what are the maximum number of children associated with male parent assurance?
df[df['sex'] == 'male']['children'].max()

#  What are the maximum number of children associated with female parent assurance?
df[df['sex'] == 'female']['children'].max()

##  Which city has the maximum female insurance total charge ?
df[(df['sex'] == 'female') & (df['charges'] == df['charges'].max())]['region']