Rails.application.routes.draw do
  namespace :admin do
    resources :employees
    resources :memberships
    resources :langages
    resources :licenses
    resources :educations
    resources :qualifications
    resources :work_shifs
    resources :job_categories
    resources :employment_statuses
    resources :grades
    resources :job_titles
    resources :organizations
    resources :nationalities
    resources :users

  end
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Defines the root path route ("/")
  # root "posts#index"
end