class CreateJobTitles < ActiveRecord::Migration[7.1]
  def change
    create_table :job_titles do |t|
      t.string :name
      t.text :description
      t.text :meta

      t.timestamps
    end
  end
end
