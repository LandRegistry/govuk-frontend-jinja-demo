curl -L https://github.com/alphagov/govuk-frontend/releases/download/v3.7.0/release-v3.7.0.zip > govuk_frontend.zip
rm -rf app/static
unzip -o govuk_frontend.zip -d app/static
mv app/static/assets/* app/static
rm -rf app/static/assets
rm -rf govuk_frontend.zip