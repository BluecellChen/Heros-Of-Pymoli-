#!/usr/bin/env python
# coding: utf-8

# In[110]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[111]:


### Player Count
purchase_data.head()


# In[112]:


# len(purchase_data["SN"].unique())
players = purchase_data["SN"].nunique() 
players


# In[113]:


# pd.DataFrame({"Total Players": [purchase_data["SN"].nunique()]})
Total_Players_df = pd.DataFrame({"Total Players": [players]})
Total_Players_df


# In[114]:


### Purchasing Analysis (Total)
items = purchase_data["Item ID"].nunique() 
items


# In[115]:


average = purchase_data["Price"].mean()


# In[116]:


purchases = purchase_data["Purchase ID"].count() 
purchases


# In[117]:


revenue = purchase_data["Price"].sum()
revenue


# In[118]:


# add currency and 2 decimal formatting 
pd.options.display.float_format = '${:,.2f}'.format

Purchasing_Analysis_df = pd.DataFrame({
    "Number of Unique Items": [items],
    "Average Price": [average], 
    "Number of Purchases": [purchases],
    "Total Revenue": [revenue]
}).round(2)

Purchasing_Analysis_df


# In[119]:


### Gender Demographics
# gender count of players
grouped_gender_df = purchase_data.groupby("Gender")
gender_count = grouped_gender_df["SN"].nunique()
gender_count


# In[120]:


# gender count and percentage of players
gender_percent = gender_count/players*100
Gender_Demographics_df = pd.DataFrame({
    "Total Count": gender_count, 
    "Percentage of Players": gender_percent
})


Gender_Demographics_df["Percentage of Players"] = Gender_Demographics_df["Percentage of Players"].map("{0:,.2f}%".format)
Gender_Demographics_df


# In[121]:


### Purchasing Analysis (Gender)
#groupby data by gender
grouped_gender_df = purchase_data.groupby("Gender")
#apply functions to columns
purchase_count = grouped_gender_df["Purchase ID"].count()
avg_purchase = grouped_gender_df["Price"].mean()
total = grouped_gender_df["Price"].sum()
avg_person = total/gender_count

#create summary data frame to hold the results
Purchasing_by_Gender_df = pd.DataFrame({
    "Purchase Count": purchase_count, 
    "Average Purchase Price": avg_purchase,
    "Total Purchase Value": total,
    "Average Purchase Total per Person": avg_person
})
Purchasing_by_Gender_df


# In[122]:


### Age Demographics

# Create bins and bin labels for ages
age_bins = [0, 9, 14, 19, 24, 29, 34, 39, 49]
age_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
# Create Data Series Into New Column Inside DataFrame
purchase_data["Age Group"] = pd.cut(purchase_data["Age"], bins=age_bins, labels=age_labels)
purchase_data
# Create a GroupBy Object Based Upon "Age Group"
age_group = purchase_data.groupby("Age Group")
#Calculate the numbers and percentages by age group
total_count_age = age_group["SN"].nunique() 
percentage_by_age = (total_count_age / players * 100).round(2)
# Create a summary DataFrame to hold the result
age_demographics_df = pd.DataFrame({
    "Total Count": total_count_age, 
    "Percentage of Players": percentage_by_age
})

age_demographics_df["Percentage of Players"] = age_demographics_df["Percentage of Players"].map("{0:,.2f}%".format)
age_demographics_df.index.name = None
age_demographics_df


# In[123]:


### Purchasing Analysis (Age)
# Create bins and bin labels for ages
age_bins = [0, 9, 14, 19, 24, 29, 34, 39, 49]
age_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
# Create Data Series Into New Column Inside DataFrame
purchase_data["Age Group"] = pd.cut(purchase_data["Age"], bins=age_bins, labels=age_labels)
purchase_data
#Calculate Purchase Count,Average Purchase Price,Total Purchase Value,Avg Total Purchase per Person by age group
purchase_count_age = age_group["SN"].count()
average_price_age = age_group["Price"].mean()
total_value_age = age_group["Price"].sum()
avg_per_person_age = (total_value_age / total_count_age)
# Create a summary DataFrame to hold the result
Purchasing_Analysis_age_df = pd.DataFrame({
    "Purchase Count": purchase_count_age,
    "Average Purchase Price": average_price_age,
    "Total Purchase Value": total_value_age,
    "Avg Total Purchase per Person": avg_per_person_age

})
Purchasing_Analysis_age_df


# In[124]:


### Top Spenders
#Run basic calculations to obtain the results in the table below
top_spenders_df = purchase_data.groupby("SN")
purchase_count = top_spenders_df["Purchase ID"].count()
avg_purchase_price = top_spenders_df["Price"].mean()
total_purchase_value = top_spenders_df["Price"].sum()
#Create a summary data frame to hold the results
Top_Spenders_df = pd.DataFrame({
    "Purchase Count": purchase_count,
    "Average Purchase Price": avg_purchase_price,
    "Total Purchase Value": total_purchase_value
})
#Sort the total purchase value column in descending order
Top_Spenders_df_sorted = Top_Spenders_df.sort_values(["Total Purchase Value"], ascending=False)
#Display a preview of the summary data frame
Top_Spenders_df_sorted.head()


# In[129]:


### Most Popular Items
#Retrieve the Item ID, Item Name, and Item Price columns
most_popular_items = purchase_data[["Item ID", "Item Name", "Price"]]
#Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
grouped_items = most_popular_items.groupby(["Item ID", "Item Name"])
#Calculate purchase count and total purchase value.
purchase_count = grouped_items["Price"].count()
total_purchase_value = grouped_items["Price"].sum()
item_price = total_purchase_value / purchase_count
#Create a summary data frame to hold the results
most_popular_items_df = pd.DataFrame({
    "Purchase Count": purchase_count,
    "Item Price":  item_price,
    "Total Purchase Value": total_purchase_value
})
#Sort the purchase count column in descending order
most_popular_items_df_sorted = most_popular_items_df.sort_values(["Purchase Count"], ascending=False)
most_popular_items_df_sorted.head()


# In[130]:


### Most Profitable Items
#Sort the above table by total purchase value in descending order
most_popular_items_df_sorted = most_popular_items_df.sort_values(["Total Purchase Value"], ascending=False)
most_popular_items_df_sorted.head()

