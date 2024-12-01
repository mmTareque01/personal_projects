class CreateOrganizations < ActiveRecord::Migration[7.1]
  def change
    create_table :organizations do |t|
      t.string :name
      t.string :reg_no
      t.string :tex_id
      t.string :phone
      t.text :address_street_1
      t.text :address_street_2
      t.string :state
      t.string :postal_code
      t.string :email
      t.string :city
      t.string :country
      t.integer :employee

      t.timestamps
    end
  end
end
