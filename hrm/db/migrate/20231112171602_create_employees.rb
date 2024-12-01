class CreateEmployees < ActiveRecord::Migration[7.1]
  def change
    create_table :employees do |t|
      t.string :f_name
      t.string :l_name
      t.string :n_name
      t.integer :e_id
      t.string :marital_status
      t.string :gender
      t.boolean :smoker
      t.date :dob
      t.references :nationality, null: false, foreign_key: true

      t.timestamps
    end
  end
end
