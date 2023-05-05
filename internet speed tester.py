import speedtest

# Prompt the user for a website URL
url = input("Enter a website URL: ")

# Test the internet speed
st = speedtest.Speedtest()
st.get_best_server()
download_speed = st.download()
upload_speed = st.upload()

# Display the results
print("Website URL: ", url)
print("Download Speed: ", round(download_speed / (10**6), 2), "Mbps")
print("Upload Speed: ", round(upload_speed / (10**6), 2), "Mbps")
