class CreateLangages < ActiveRecord::Migration[7.1]
  def change
    create_table :langages do |t|
      t.string :name
      t.text :meta

      t.timestamps
    end
  end
end
