# altana_ai
1. Use a virtiual environment to avoid dependency issues
2. Install the requirements by running 
    
        pip install -r requirements.txt
    
3. Create the db table in postgres by running the file csv_to_sql.py
    
        python csv_to_sql.py
    
    Note: Change the url of the postgres table in line 6
4. Run the api file 
   Note: Change the url of the postgres table
    
        python api.py
    
5. Open a browser and enter the url that is displayed on the terminal with the extension based on the get request
   
   a. To get all companies associated with a given operator add the extension
    
        /companies/<operator_name>
        
    b. To get all operators associated with a given company add the extension
    
        /operators/<company_name>
        
    c. To get all companies connected to a given company via shared operators add the extension
    
        /all_companies/<company_name>

Architecture

1. I used a postgres database to store the data. 
2. I built a flask api for the get requests since it is highly scalable and easy to use. It was also straightforward to integrate flask with postgres

Challenges

The data had some discrepancies like columns were not split in the csv and so when I created a db I initally faced the issue where the entire data appeared as a single column.
I solved this by cleaning up the data and dropped empty columns that were created in the process
