json.extract! employee, :id, :f_name, :l_name, :n_name, :e_id, :marital_status, :gender, :smoker, :dob, :nationality_id, :created_at, :updated_at
json.url employee_url(employee, format: :json)
