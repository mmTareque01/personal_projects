class WorkShifsController < ApplicationController
  before_action :set_work_shif, only: %i[ show edit update destroy ]

  # GET /work_shifs or /work_shifs.json
  def index
    @work_shifs = WorkShif.all
  end

  # GET /work_shifs/1 or /work_shifs/1.json
  def show
  end

  # GET /work_shifs/new
  def new
    @work_shif = WorkShif.new
  end

  # GET /work_shifs/1/edit
  def edit
  end

  # POST /work_shifs or /work_shifs.json
  def create
    @work_shif = WorkShif.new(work_shif_params)

    respond_to do |format|
      if @work_shif.save
        format.html { redirect_to work_shif_url(@work_shif), notice: "Work shif was successfully created." }
        format.json { render :show, status: :created, location: @work_shif }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @work_shif.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /work_shifs/1 or /work_shifs/1.json
  def update
    respond_to do |format|
      if @work_shif.update(work_shif_params)
        format.html { redirect_to work_shif_url(@work_shif), notice: "Work shif was successfully updated." }
        format.json { render :show, status: :ok, location: @work_shif }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @work_shif.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /work_shifs/1 or /work_shifs/1.json
  def destroy
    @work_shif.destroy!

    respond_to do |format|
      format.html { redirect_to work_shifs_url, notice: "Work shif was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_work_shif
      @work_shif = WorkShif.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def work_shif_params
      params.require(:work_shif).permit(:name, :from, :to)
    end
end
