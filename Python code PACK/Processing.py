
import pandas as pd


"""	ROI info	"""

# Read Info about ROI

data = pd.read_csv('calendar_date.csv')
data = data.rename(columns={'0': 'day', '2019-09-01': 'date', '310': 'source', '0.02': 'profit', 'Unnamed: 4': 'cost'})
data['cost'] = data["cost"].fillna(0)

# Days Split

data_day0 = data[data['day'] == 0]
data_day0 = data_day0.drop('day', axis = 1)

data_day1 = data[data['day'] == 1]
data_day1 = data_day1.drop('day', axis = 1)

data_day2 = data[data['day'] == 2]
data_day2 = data_day2.drop('day', axis = 1)

data_day3 = data[data['day'] == 3]
data_day3 = data_day3.drop('day', axis = 1)

# Merge days table to MAIN-DATA-TABLE

train = pd.merge(data_day1, data_day0,  on=['source','date', 'cost'], how='right')
train = train.rename(columns={'profit_x':'profit_1_day', 'profit_y':'profit_0_day'})
train["profit_1_day"] = train["profit_1_day"].fillna(0) 

train = pd.merge(data_day2, train,  on=['source','date', 'cost'], how='right')
train = train.rename(columns={'profit':'profit_2_day'})
train["profit_2_day"] = train["profit_2_day"].fillna(0) 

train = pd.merge(data_day3, train,  on=['source','date', 'cost'], how='right')
train = train.rename(columns={'profit':'profit_3_day'})
train["profit_3_day"] = train["profit_3_day"].fillna(0) 

# Transform columns in the data
train = train[['date', 'source', 'cost', 'profit_0_day', 'profit_1_day','profit_2_day','profit_3_day']]

print("Part 1 completed! ")


"""	Count Clicks, Retentions	"""


clicks = pd.read_csv("count_clicks_data-UserCreated.csv")
clicks = clicks.rename(columns={'0':'day', '2019-11-17':'date', 'Unnamed: 2':'source', '1':'click', 'send_sex_request_btn':'attr'})
clicks = clicks.dropna()


# Days Split

data_day0 = clicks[clicks['day'] == 0]
data_day0 = data_day0.drop('day', axis = 1)

data_day1 = clicks[clicks['day'] == 1]
data_day1 = data_day1.drop('day', axis = 1)

data_day2 = clicks[clicks['day'] == 2]
data_day2 = data_day2.drop('day', axis = 1)

data_day3 = clicks[clicks['day'] == 3]
data_day3 = data_day3.drop('day', axis = 1)


"""	2.1 Chat Invite """
chat_invite0 = data_day0[data_day0['attr'] == 'chat_invite']
chat_invite1 = data_day1[data_day1['attr'] == 'chat_invite']
chat_invite2 = data_day2[data_day2['attr'] == 'chat_invite']
chat_invite3 = data_day3[data_day3['attr'] == 'chat_invite']

chat_invite0 = chat_invite0.drop('attr', axis = 1)
chat_invite1 = chat_invite1.drop('attr', axis = 1)
chat_invite2 = chat_invite2.drop('attr', axis = 1)
chat_invite3 = chat_invite3.drop('attr', axis = 1)

chat_invite = pd.merge(chat_invite1, chat_invite0,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click_x':'chat_invite_1_day', 'click_y':'chat_invite_0_day'})
chat_invite["chat_invite_1_day"] = chat_invite["chat_invite_1_day"].fillna(0) 

chat_invite = pd.merge(chat_invite2, chat_invite,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click':'chat_invite_2_day'})
chat_invite["chat_invite_2_day"] = chat_invite["chat_invite_2_day"].fillna(0) 

chat_invite = pd.merge(chat_invite3, chat_invite,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click':'chat_invite_3_day'})
chat_invite["chat_invite_3_day"] = chat_invite["chat_invite_3_day"].fillna(0)

chat_invite = chat_invite[['date', 'source', 'chat_invite_0_day', 'chat_invite_1_day','chat_invite_2_day','chat_invite_3_day']]


"""	2.2 Charlist _bnr """

data_step2 = pd.merge(chat_invite, train,  on=['source','date'], how='right')
data_day0 = clicks[clicks['day'] == 0]
data_day0 = data_day0.drop('day', axis = 1)

data_day1 = clicks[clicks['day'] == 1]
data_day1 = data_day1.drop('day', axis = 1)

data_day2 = clicks[clicks['day'] == 2]
data_day2 = data_day2.drop('day', axis = 1)

data_day3 = clicks[clicks['day'] == 3]
data_day3 = data_day3.drop('day', axis = 1)

chat_invite0 = data_day0[data_day0['attr'] == 'chatlist_bnr']
chat_invite1 = data_day1[data_day1['attr'] == 'chatlist_bnr']
chat_invite2 = data_day2[data_day2['attr'] == 'chatlist_bnr']
chat_invite3 = data_day3[data_day3['attr'] == 'chatlist_bnr']

chat_invite0 = chat_invite0.drop('attr', axis = 1)
chat_invite1 = chat_invite1.drop('attr', axis = 1)
chat_invite2 = chat_invite2.drop('attr', axis = 1)
chat_invite3 = chat_invite3.drop('attr', axis = 1)

chat_invite = pd.merge(chat_invite1, chat_invite0,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click_x':'chatlist_bnr_1_day', 'click_y':'chatlist_bnr_0_day'})
chat_invite["chatlist_bnr_1_day"] = chat_invite["chatlist_bnr_1_day"].fillna(0) 

chat_invite = pd.merge(chat_invite2, chat_invite,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click':'chatlist_bnr_2_day'})
chat_invite["chatlist_bnr_2_day"] = chat_invite["chatlist_bnr_2_day"].fillna(0) 

chat_invite = pd.merge(chat_invite3, chat_invite,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click':'chatlist_bnr_3_day'})
chat_invite["chatlist_bnr_3_day"] = chat_invite["chatlist_bnr_3_day"].fillna(0)

chat_invite = chat_invite[['date', 'source', 'chatlist_bnr_0_day', 'chatlist_bnr_1_day','chatlist_bnr_2_day','chatlist_bnr_3_day']]

data_step3 = pd.merge(chat_invite, data_step2, on=['source','date'], how='right')



"""	2.3 Charlist livecamps """

data_day0 = clicks[clicks['day'] == 0]
data_day0 = data_day0.drop('day', axis = 1)

data_day1 = clicks[clicks['day'] == 1]
data_day1 = data_day1.drop('day', axis = 1)

data_day2 = clicks[clicks['day'] == 2]
data_day2 = data_day2.drop('day', axis = 1)

data_day3 = clicks[clicks['day'] == 3]
data_day3 = data_day3.drop('day', axis = 1)

chat_invite0 = data_day0[data_day0['attr'] == 'livecamps']
chat_invite1 = data_day1[data_day1['attr'] == 'livecamps']
chat_invite2 = data_day2[data_day2['attr'] == 'livecamps']
chat_invite3 = data_day3[data_day3['attr'] == 'livecamps']

chat_invite0 = chat_invite0.drop('attr', axis = 1)
chat_invite1 = chat_invite1.drop('attr', axis = 1)
chat_invite2 = chat_invite2.drop('attr', axis = 1)
chat_invite3 = chat_invite3.drop('attr', axis = 1)

chat_invite = pd.merge(chat_invite1, chat_invite0,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click_x':'livecamps_bnr_1_day', 'click_y':'livecamps_bnr_0_day'})
chat_invite["livecamps_bnr_1_day"] = chat_invite["livecamps_bnr_1_day"].fillna(0) 

chat_invite = pd.merge(chat_invite2, chat_invite,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click':'livecamps_bnr_2_day'})
chat_invite["livecamps_bnr_2_day"] = chat_invite["livecamps_bnr_2_day"].fillna(0) 

chat_invite = pd.merge(chat_invite3, chat_invite,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click':'livecamps_bnr_3_day'})
chat_invite["livecamps_bnr_3_day"] = chat_invite["livecamps_bnr_3_day"].fillna(0)

chat_invite = chat_invite[['date', 'source', 'livecamps_bnr_0_day', 'livecamps_bnr_1_day','livecamps_bnr_2_day','livecamps_bnr_3_day']]

data_step4 = pd.merge(chat_invite, data_step3, on=['source','date'], how='right')



"""	2.4 accept_sex_request_btn """

data_day0 = clicks[clicks['day'] == 0]
data_day0 = data_day0.drop('day', axis = 1)

data_day1 = clicks[clicks['day'] == 1]
data_day1 = data_day1.drop('day', axis = 1)

data_day2 = clicks[clicks['day'] == 2]
data_day2 = data_day2.drop('day', axis = 1)

data_day3 = clicks[clicks['day'] == 3]
data_day3 = data_day3.drop('day', axis = 1)

chat_invite0 = data_day0[data_day0['attr'] == 'accept_sex_request_btn']
chat_invite1 = data_day1[data_day1['attr'] == 'accept_sex_request_btn']
chat_invite2 = data_day2[data_day2['attr'] == 'accept_sex_request_btn']
chat_invite3 = data_day3[data_day3['attr'] == 'accept_sex_request_btn']

chat_invite0 = chat_invite0.drop('attr', axis = 1)
chat_invite1 = chat_invite1.drop('attr', axis = 1)
chat_invite2 = chat_invite2.drop('attr', axis = 1)
chat_invite3 = chat_invite3.drop('attr', axis = 1)

chat_invite = pd.merge(chat_invite1, chat_invite0,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click_x':'accept_sex_request_btn_1_day', 'click_y':'accept_sex_request_btn_0_day'})
chat_invite["accept_sex_request_btn_1_day"] = chat_invite["accept_sex_request_btn_1_day"].fillna(0) 

chat_invite = pd.merge(chat_invite2, chat_invite,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click':'accept_sex_request_btn_2_day'})
chat_invite["accept_sex_request_btn_day"] = chat_invite["accept_sex_request_btn_2_day"].fillna(0) 

chat_invite = pd.merge(chat_invite3, chat_invite,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click':'accept_sex_request_btn_3_day'})
chat_invite["accept_sex_request_btn_3_day"] = chat_invite["accept_sex_request_btn_3_day"].fillna(0)

chat_invite = chat_invite[['date', 'source', 'accept_sex_request_btn_0_day', 'accept_sex_request_btn_1_day','accept_sex_request_btn_2_day','accept_sex_request_btn_3_day']]

data_step5 = pd.merge(chat_invite, data_step4, on=['source','date'], how='right')


"""	2.5 sent_sex_request_btn """

data_day0 = clicks[clicks['day'] == 0]
data_day0 = data_day0.drop('day', axis = 1)

data_day1 = clicks[clicks['day'] == 1]
data_day1 = data_day1.drop('day', axis = 1)

data_day2 = clicks[clicks['day'] == 2]
data_day2 = data_day2.drop('day', axis = 1)

data_day3 = clicks[clicks['day'] == 3]
data_day3 = data_day3.drop('day', axis = 1)

chat_invite0 = data_day0[data_day0['attr'] == 'sent_sex_request_btn']
chat_invite1 = data_day1[data_day1['attr'] == 'sent_sex_request_btn']
chat_invite2 = data_day2[data_day2['attr'] == 'sent_sex_request_btn']
chat_invite3 = data_day3[data_day3['attr'] == 'sent_sex_request_btn']

chat_invite0 = chat_invite0.drop('attr', axis = 1)
chat_invite1 = chat_invite1.drop('attr', axis = 1)
chat_invite2 = chat_invite2.drop('attr', axis = 1)
chat_invite3 = chat_invite3.drop('attr', axis = 1)

chat_invite = pd.merge(chat_invite1, chat_invite0,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click_x':'sent_sex_request_btn_1_day', 'click_y':'sent_sex_request_btn_0_day'})
chat_invite["sent_sex_request_btn_1_day"] = chat_invite["sent_sex_request_btn_1_day"].fillna(0) 

chat_invite = pd.merge(chat_invite2, chat_invite,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click':'sent_sex_request_btn_2_day'})
chat_invite["sent_sex_request_btn_day"] = chat_invite["sent_sex_request_btn_2_day"].fillna(0) 

chat_invite = pd.merge(chat_invite3, chat_invite,  on=['source','date'], how='right')
chat_invite = chat_invite.rename(columns={'click':'sent_sex_request_btn_3_day'})
chat_invite["sent_sex_request_btn_3_day"] = chat_invite["sent_sex_request_btn_3_day"].fillna(0)

chat_invite = chat_invite[['date', 'source', 'sent_sex_request_btn_0_day', 'sent_sex_request_btn_1_day','sent_sex_request_btn_2_day','sent_sex_request_btn_3_day']]

data_step6 = pd.merge(chat_invite, data_step5, on=['source','date'], how='right')




""" ****************************************************** ********************************************************** ************************** """
data_step6 = data_step6.fillna(0)

data_step6 = data_step6[['date',
       'source', 'cost', 'profit_0_day',
       'profit_1_day', 'profit_2_day', 'profit_3_day', 'sent_sex_request_btn_0_day', 'sent_sex_request_btn_1_day',
       'sent_sex_request_btn_2_day', 'sent_sex_request_btn_3_day', 'accept_sex_request_btn_0_day',
       'accept_sex_request_btn_1_day', 'accept_sex_request_btn_2_day',
       'accept_sex_request_btn_3_day', 'livecamps_bnr_0_day',
       'livecamps_bnr_1_day', 'livecamps_bnr_2_day', 'livecamps_bnr_3_day',
       'chatlist_bnr_0_day', 'chatlist_bnr_1_day', 'chatlist_bnr_2_day',
       'chatlist_bnr_3_day', 'chat_invite_0_day', 'chat_invite_1_day','chat_invite_2_day','chat_invite_3_day']]

print("Part 2 completed! ")


"""	Part 3: User Created """
user_created = pd.read_csv("users_created.csv")

user_created = user_created.rename(columns={'push':'source', '2019-09-01':'date', '4':'count_users'})
user_created = user_created[['date', 'source', 'count_users']]
user_created = user_created.fillna(0)

user_created['source'] = pd.to_numeric(user_created['source'], errors='coerce')
train_data = pd.merge(user_created, data_step6, on=['source','date'], how='right')

print("Part 3 completed! ")



"""	Part 4: User visited """

user_visit = pd.read_csv("user_visit.csv")
user_visit = user_visit.rename(columns={'0':'day', 'Unnamed: 1':'source', '2019-09-01':'date', '58':'count_visit'})
user_visit = user_visit.fillna(0)

data_day0 = user_visit[user_visit['day'] == 0]
data_day0 = data_day0.drop('day', axis = 1)

data_day1 = user_visit[user_visit['day'] == 1]
data_day1 = data_day1.drop('day', axis = 1)

data_day2 = user_visit[user_visit['day'] == 2]
data_day2 = data_day2.drop('day', axis = 1)

data_day3 = user_visit[user_visit['day'] == 3]
data_day3 = data_day3.drop('day', axis = 1)


user_visit = pd.merge(data_day1, data_day0,  on=['source','date'], how='right')
user_visit = user_visit.rename(columns={'count_visit_x':'visit_1_day', 'count_visit_y':'visit_0_day'})
user_visit["visit_1_day"] = user_visit["visit_1_day"].fillna(0) 

user_visit = pd.merge(data_day2, user_visit,  on=['source','date'], how='right')
user_visit = user_visit.rename(columns={'count_visit':'visit_2_day'})
user_visit["visit_2_day"] = user_visit["visit_2_day"].fillna(0) 

user_visit = pd.merge(data_day3, user_visit,  on=['source','date'], how='right')
user_visit = user_visit.rename(columns={'count_visit':'visit_3_day'})
user_visit["visit_3_day"] = user_visit["visit_3_day"].fillna(0) 

user_visit = user_visit[['source', 'date', 'visit_0_day', 'visit_1_day', 'visit_2_day',
       'visit_3_day']]

time_data = user_visit.drop(user_visit[user_visit['source'] == '{affiliate_id}'].index)
time_data = time_data.drop(time_data[time_data['source'] == 'email'].index)
time_data = time_data.drop(time_data[time_data['source'] == '{host}'].index)
time_data = time_data.drop(time_data[time_data['source'] == 'test'].index)
time_data = time_data.drop(time_data[time_data['source'] == 'xuichee'].index)

user_visit['source'] = time_data['source'].astype(float)

finally_data = pd.merge(user_visit, train_data,  on=['source','date'], how='right')

finally_data = finally_data.fillna(0)

finally_data = finally_data[['source', 'date', 'count_users', 'cost', 'profit_0_day', 'profit_1_day',
       'profit_2_day', 'profit_3_day', 'visit_0_day', 'visit_1_day', 'visit_2_day',
       'visit_3_day', 'sent_sex_request_btn_0_day',
       'sent_sex_request_btn_1_day', 'sent_sex_request_btn_2_day',
       'sent_sex_request_btn_3_day', 'accept_sex_request_btn_0_day',
       'accept_sex_request_btn_1_day', 'accept_sex_request_btn_2_day',
       'accept_sex_request_btn_3_day', 'livecamps_bnr_0_day',
       'livecamps_bnr_1_day', 'livecamps_bnr_2_day', 'livecamps_bnr_3_day',
       'chatlist_bnr_0_day', 'chatlist_bnr_1_day', 'chatlist_bnr_2_day',
       'chatlist_bnr_3_day', 'chat_invite_0_day', 'chat_invite_1_day',
       'chat_invite_2_day', 'chat_invite_3_day']]


print("Finish! Basta! 	Yepta!")
print(finally_data.head(50))
