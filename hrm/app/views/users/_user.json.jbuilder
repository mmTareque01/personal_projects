json.extract! user, :id, :username, :role, :employee_name, :status, :created_at, :updated_at
json.url user_url(user, format: :json)
