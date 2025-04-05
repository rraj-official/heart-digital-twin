# Step 6: Run docker-compose to bring up the containers
cd DTaaS/deploy/docker
echo "Running docker-compose to bring up the containers..."
sudo docker-compose -f compose.local.yml --env-file .env.local up -d
if [ $? -ne 0 ]; then
  echo "Failed to start Docker containers. Exiting..."
  exit 1
fi

# Step 6.5 Cool Loading animation

# Function to display the loading animation
echo "Opening localhost in your default browser..."
loading_animation() {
  local pid=$1
  local delay=0.1
  local spinstr='|/-\\'
  
  while kill -0 "$pid" 2>/dev/null; do
    for i in `seq 0 3`; do
      echo -n "${spinstr:$i:1}"  # Display one character at a time
      sleep $delay
      echo -ne "\r"  # Move cursor to beginning of the line
    done
  done
  echo -ne "\r"  # Clear the spinner once done
}

# Start a background process (for example, sleeping for 3 seconds)
(sleep 3) &

# Capture the PID of the background process
pid=$!

# Call the loading animation function while the background process runs
loading_animation $pid

# Output after the sleep is done
echo "Done!"

# Step 7: Open localhost in default browser
xdg-open http://localhost || echo "Failed to open browser. You can visit http://localhost manually."

echo "Setup completed successfully!"
