class CreateWorkShifs < ActiveRecord::Migration[7.1]
  def change
    create_table :work_shifs do |t|
      t.string :name
      t.date :from
      t.date :to

      t.timestamps
    end
  end
end
