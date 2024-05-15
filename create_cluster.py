import requests
import json

def login(username, password):
    url = "https://CommandCenterHostName/commandcenter/api/Login"
    payload = json.dumps({
        "username": username,
        "password": password
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response

def add_kubernetes_cluster(auth_token, cluster_name):
    url = "https://CommandCenterHostName/commandcenter/api/V4/Kubernetes/cluster"
    payload = json.dumps({
        "name": cluster_name,
        "skipCredentialValidation": True,
        "accessNodes": [{"id": 0, "name": "string", "displayName": "string", "type": 0}],
        "credentials": {"id": 0, "name": "string"},
        "etcdProtection": {"enabled": True, "plan": {"id": 0, "name": "string"}},
        "planEntity": {"id": 0, "name": "string"},
        "hypervisorType": "KUBERNETES",
        "endpointurl": "string",
        "serviceName": "string",
        "secretKey": "string",
        "userName": "string",
        "password": "string",
        "k8ServiceType": "ONPREM"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authtoken': auth_token
    }
    response = requests.post(url, headers=headers, data=payload)
    return response

def main():
    username = "your_username"
    password = "your_password"
    cluster_name = "your_cluster_name"

    # Login
    login_response = login(username, password)
    if login_response.status_code == 200:
        print("Login successful")
        auth_token = login_response.json().get("token")
    else:
        print("Login failed with status code:", login_response.status_code)
        print("Response:", login_response.text)
        return

    # Add Kubernetes Cluster
    cluster_response = add_kubernetes_cluster(auth_token, cluster_name)
    print(cluster_response.text)

if __name__ == "__main__":
    main()
