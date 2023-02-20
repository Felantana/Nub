import pandas as pd
import swagger_client.compass_lib as compass

def pull_accounts(configuration, min_req: int, limit=999, iterations_to_reconnect = 250):

    query = {"requestedDtm": {"op": "nempty"}}
    api_response = compass.get_requests2(configuration=configuration,q=query)
    
    upper_bound = int(api_response.to_dict()['items'][0]['request_id'])
    lower_bound = upper_bound - limit
    #requests_df = pd.DataFrame()
    list_dfs = []
    iteration = 1

    while upper_bound > min_req:
        
        if upper_bound <= 99999 and upper_bound > 25216:
            upper_bound = 25216
            lower_bound = max(upper_bound - limit, min_req)
            
        
        query = {"requestId": {"op": "range", "start": lower_bound,"end":upper_bound}}

        api_response = compass.get_requests2(configuration=configuration,q=query)
        try:
            if len(api_response.to_dict()['items']) != 0:
                df = pd.DataFrame(api_response.to_dict()['items'])
                list_dfs.append(df)
                #requests_df = pd.concat([requests_df,pd.DataFrame(api_response.to_dict()['items'])])
                print(f"Iteration # {iteration}: Range: {lower_bound} - {upper_bound}: Done - {len(df)} accounts retrieved")
            else:
                print(f"Iteration # {iteration}: Range: {lower_bound} - {upper_bound}: No accounts retrieved")
            #break
        except:
            pass

        
        upper_bound = lower_bound
        lower_bound = max(upper_bound - limit, min_req)
        
        
        iteration += 1

        if iteration % iterations_to_reconnect == 0:
            access_token,configuration,user_info = compass.init_conn()
    
    requests_df = pd.concat(list_dfs).drop_duplicates() 
    print(requests_df.shape[0]," accounts retrieved")

    return requests_df