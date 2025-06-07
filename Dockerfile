# --- Build Stage ---
FROM node:20-alpine as build

WORKDIR /opt/qr-page-react

COPY qr-page-react/package*.json ./
RUN npm install

COPY qr-page-react .

RUN npm run build

# --- Production Stage ---
FROM nginx:alpine as production

# Copy the static build output from the build stage
COPY --from=build /opt/qr-page-react/dist /usr/share/nginx/html

# Copy a custom Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Expose the port Nginx will be listening on
EXPOSE 80

# Use the custom entrypoint script to generate env-config.js before starting Nginx
ENTRYPOINT ["/docker-entrypoint.sh"]
# The original Nginx command is passed as arguments to the entrypoint script
CMD ["nginx", "-g", "daemon off;"]