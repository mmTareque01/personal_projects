class CreateUsers < ActiveRecord::Migration[7.1]
  def change
    create_table :users do |t|
      t.string :username
      t.string :role
      t.string :employee_name
      t.string :status

      t.timestamps
    end
  end
end
