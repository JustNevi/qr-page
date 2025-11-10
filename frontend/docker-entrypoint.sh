#!/bin/sh
# This script will run when the Docker container starts

echo "Generating /usr/share/nginx/html/env-config.js..."

# Start the JavaScript object
echo "window._env_ = {" > /usr/share/nginx/html/env-config.js

# Iterate over all environment variables that start with VITE_
# Use `env` command and pipe to grep for VITE_ prefix
# Then use sed to format and escape for JavaScript
env | grep '^VITE_' | while IFS='=' read -r var_name var_value; do
  # Escape double quotes and backslashes in the variable value
  # This prevents syntax errors in the generated JavaScript
  # The sed command is crucial here
  escaped_value=$(echo "$var_value" | sed -e 's/[\/&]/\\&/g; s/"/\\"/g')
  echo "  $var_name: \"$escaped_value\"," >> /usr/share/nginx/html/env-config.js
done

# End the JavaScript object
echo "};" >> /usr/share/nginx/html/env-config.js

echo "Generated env-config.js content:"
cat /usr/share/nginx/html/env-config.js

# Execute the original Nginx command passed as arguments to the entrypoint
exec "$@"