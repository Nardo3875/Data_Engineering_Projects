import requests
import base64
import matplotlib.pyplot as plt
import pandas as pd

def get_drug_interactions(drug1, drug2, api_key):
    base_url = "https://api.fda.gov/drug/event.json"

    # Set up headers for the API request with basic authentication
    headers = {
        'Authorization': f'Basic {base64.b64encode(api_key.encode()).decode()}'
    }

    # Set up parameters for the API request
    params = {
        'search': f'patient.drug.medicinalproduct:"{drug1}" AND patient.drug.medicinalproduct:"{drug2}"'
    }

    try:
        # Make the API request 
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()  

        
        data = response.json()

        
        results = data.get('results', [])
        
        if results:
            interactions = [item['patient']['drug'] for item in results]
            return interactions
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None

def extract_pharm_classes(interactions):
    extracted_data = []

    for interaction in interactions:
        for drug in interaction:
            extracted_data.append({
                'drugcharacterization': drug.get('drugcharacterization', ''),
                'medicinalproduct': drug.get('medicinalproduct', ''),
                'pharm_class_epc': drug.get('openfda', {}).get('pharm_class_epc', [])
            })

    return extracted_data

if __name__ == "__main__":
   # Enter your personal API Key bellow 
    api_key = ''

    # Example Medication
    drug1 = "aspirin"
    drug2 = "ibuprofen"

    # Medication interactions
    interactions = get_drug_interactions(drug1, drug2, api_key)

    if interactions:
        # Extract relevant information for DataFrame
        extracted_data = extract_pharm_classes(interactions)

        # Create a Pandas DataFrame
        df = pd.DataFrame(extracted_data)

        # Display the DataFrame
        print("\nDataFrame of Drug Interactions:")
        print(df.describe())

        # Visualize interactions with a pie chart
        if 'pharm_class_epc' in df.columns:
            interaction_types = df['pharm_class_epc'].explode()
            interaction_counts = interaction_types.value_counts()

            # Create a pie chart
            plt.pie(interaction_counts.values, labels=interaction_counts.index, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')  
            plt.title('Drug Interactions by Pharmaceutical Class')
            plt.show()
            
        else:
            print("No 'pharm_class_epc' column found in the DataFrame.")
    else:
        print("Failed to retrieve drug interactions.")
