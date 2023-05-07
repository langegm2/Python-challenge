#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
import os

file_to_load = os.path.join(".","Resources","election_data.csv")
file_to_output = os.path.join(".", "election_analysis.txt")


total_votes = 0

candidate_votes={}

candidate_options=[]

winning_candidate = ""
winning_count = 0

with open(file_to_load) as election_data:
    
    reader= csv.reader(election_data)
    header= next(reader)
    
    for row in reader:
        total_votes= total_votes + 1
        candidate_name= row[2]
        
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        
with open(file_to_output, "w") as text_file:
    election_results = (
        f"election results\n"
        f"--------------\n"
        f"total votes {total_votes}\n:"
        f"----------------\n"
    )
    
    print(election_results, end ="")
    
    #txt_file.write(election_results)
    
    for candidate in candidate_votes:
        
        votes = candidate_votes[candidate]
        vote_percentage= float(votes) / float(total_votes) * 100
        
        if(votes> winning_count):
            winning_count= votes
            winning_candidate = candidate
            
        voter_output = f"{candidate}: {vote_percentage: .3f}% ({votes})\n"
        
        print(voter_output, end = "")
        
        text_file.write(voter_output)
        
    winning_candidate_summary = (
    
        f"-----------------\n"
        f"winner: {winning_candidate}\n"
        f"-----------------\n"
    )
     
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)
        


# In[ ]:





# In[ ]:




