headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer cfecb34e-43a7-4f0c-b121-ecd957e5174f'}

print('sending get request to http://localhost:7000/statistics/Test2')
response = requests.get('http://localhost:7000/statistics/Test2', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '[{"id":null,"date":"2019-01-21T00:00:00.000+0000"},"incomes":[{"title":"Salary","amount":95.8267},{"title":"Scholarship","amount":16.4275}],"expenses":[{"title":"Utilities","amount":6.5710},{"title":"Vacation","amount":9.3653},{"title":"Phone","amount":0.3746},{"title":"Meal","amount":100.0000},{"title":"Gas","amount":1.9713},{"title":"Rent","amount":19.7130}],"statistics":{"EXPENSES_AMOUNT":137.9952,"INCOMES_AMOUNT":112.2542,"SAVING_AMOUNT":2000.00000},"rates":{"EUR":0.8770391159,"RUB":66.3275741098,"USD":1}}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

