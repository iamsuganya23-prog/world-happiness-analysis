import pandas as pd
import matplotlib.pyplot as plt

path = 'C:/Users/HP/OneDrive/Desktop/New folder (2)/Self study/python/'

df2015 = pd.read_csv(path + '2015.csv')
df2016 = pd.read_csv(path + '2016.csv')
df2017 = pd.read_csv(path + '2017.csv')
df2018 = pd.read_csv(path + '2018.csv')
df2019 = pd.read_csv(path + '2019.csv')

df2015 = df2015[['Country','Happiness Rank','Happiness Score','Economy (GDP per Capita)','Health (Life Expectancy)','Freedom','Generosity']].copy()
df2015.columns = ['Country','Rank','Score','GDP','Health','Freedom','Generosity']
df2015['Year'] = 2015

df2016 = df2016[['Country','Happiness Rank','Happiness Score','Economy (GDP per Capita)','Health (Life Expectancy)','Freedom','Generosity']].copy()
df2016.columns = ['Country','Rank','Score','GDP','Health','Freedom','Generosity']
df2016['Year'] = 2016

df2017 = df2017[['Country','Happiness.Rank','Happiness.Score','Economy..GDP.per.Capita.','Health..Life.Expectancy.','Freedom','Generosity']].copy()
df2017.columns = ['Country','Rank','Score','GDP','Health','Freedom','Generosity']
df2017['Year'] = 2017

df2018 = df2018[['Country or region','Overall rank','Score','GDP per capita','Healthy life expectancy','Freedom to make life choices','Generosity']].copy()
df2018.columns = ['Country','Rank','Score','GDP','Health','Freedom','Generosity']
df2018['Year'] = 2018

df2019 = df2019[['Country or region','Overall rank','Score','GDP per capita','Healthy life expectancy','Freedom to make life choices','Generosity']].copy()
df2019.columns = ['Country','Rank','Score','GDP','Health','Freedom','Generosity']
df2019['Year'] = 2019

df = pd.concat([df2015,df2016,df2017,df2018,df2019],ignore_index=True)

top10 = df[df['Year']==2019].nsmallest(10,'Rank')
plt.figure(figsize=(10,6))
plt.barh(top10['Country'], top10['Score'], color='steelblue')
plt.xlabel('Happiness Score')
plt.title('Top 10 Happiest Countries in 2019')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('chart1_top10.png')
plt.show()
print('Chart 1 done!')


# Chart 2 - Average happiness score by year
yearly = df.groupby('Year')['Score'].mean()
plt.figure(figsize=(8,5))
plt.plot(yearly.index, yearly.values, marker='o', color='green', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Average Happiness Score')
plt.title('World Average Happiness Score (2015-2019)')
plt.tight_layout()
plt.savefig('chart2_yearly.png')
plt.show()
print('Chart 2 done!')

# Chart 3 - Top 5 countries average score
top5 = df.groupby('Country')['Score'].mean().nlargest(5)
plt.figure(figsize=(8,5))
plt.bar(top5.index, top5.values, color='coral')
plt.xlabel('Country')
plt.ylabel('Average Happiness Score')
plt.title('Top 5 Happiest Countries (2015-2019 Average)')
plt.tight_layout()
plt.savefig('chart3_top5.png')
plt.show()
print('Chart 3 done!')

# Chart 4 - GDP vs Happiness Score scatter plot
plt.figure(figsize=(8,5))
plt.scatter(df['GDP'], df['Score'], alpha=0.5, color='purple')
plt.xlabel('GDP per Capita')
plt.ylabel('Happiness Score')
plt.title('GDP vs Happiness Score (2015-2019)')
plt.tight_layout()
plt.savefig('chart4_gdp_vs_happiness.png')
plt.show()
print('Chart 4 done!')

# Key insights
print('\n--- KEY INSIGHTS ---')
print('Happiest country in 2019:', df[df['Year']==2019].nsmallest(1,'Rank')['Country'].values[0])
print('Least happy country in 2019:', df[df['Year']==2019].nlargest(1,'Rank'))
