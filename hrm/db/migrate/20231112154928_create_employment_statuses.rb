class CreateEmploymentStatuses < ActiveRecord::Migration[7.1]
  def change
    create_table :employment_statuses do |t|
      t.string :name
      t.text :meta

      t.timestamps
    end
  end
end
