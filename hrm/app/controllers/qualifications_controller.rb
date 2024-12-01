class QualificationsController < ApplicationController
  before_action :set_qualification, only: %i[ show edit update destroy ]

  # GET /qualifications or /qualifications.json
  def index
    @qualifications = Qualification.all
  end

  # GET /qualifications/1 or /qualifications/1.json
  def show
  end

  # GET /qualifications/new
  def new
    @qualification = Qualification.new
  end

  # GET /qualifications/1/edit
  def edit
  end

  # POST /qualifications or /qualifications.json
  def create
    @qualification = Qualification.new(qualification_params)

    respond_to do |format|
      if @qualification.save
        format.html { redirect_to qualification_url(@qualification), notice: "Qualification was successfully created." }
        format.json { render :show, status: :created, location: @qualification }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @qualification.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /qualifications/1 or /qualifications/1.json
  def update
    respond_to do |format|
      if @qualification.update(qualification_params)
        format.html { redirect_to qualification_url(@qualification), notice: "Qualification was successfully updated." }
        format.json { render :show, status: :ok, location: @qualification }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @qualification.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /qualifications/1 or /qualifications/1.json
  def destroy
    @qualification.destroy!

    respond_to do |format|
      format.html { redirect_to qualifications_url, notice: "Qualification was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_qualification
      @qualification = Qualification.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def qualification_params
      params.require(:qualification).permit(:name, :description, :meta)
    end
end
