class CreateQualifications < ActiveRecord::Migration[7.1]
  def change
    create_table :qualifications do |t|
      t.string :name
      t.text :description
      t.text :meta

      t.timestamps
    end
  end
end
