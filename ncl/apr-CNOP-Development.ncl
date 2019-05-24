;----------------------------------------------------------------------
; panel_33.ncl
;
; Concepts illustrated:
;   - Combining two sets of paneled plots on one page
;   - Maximizing paneled plots after they've been created
;   - Drawing two labelbars in a combined panel plot
;----------------------------------------------------------------------
;
; These files are loaded by default in NCL V6.2.0 and newer
; load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
; load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
; load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"

begin
;---Open file
    fname = "/BIGDATA1/iocas_mmu_2/PPSO_qin/record/cp-APR/3_29_ocean.nc"
    f     = addfile(fname, "r")
    fname_origin_p = "/BIGDATA1/iocas_mmu_2/GFDL-CM2p1/output/04210101.ocean_month.nc"
    fname_origin_n = "/BIGDATA1/iocas_mmu_2/GFDL-CM2p1/output/04260101.ocean_month.nc"
    f_f     = addfile(fname_origin_p, "r")
    f_n     = addfile(fname_origin_n, "r")
    month_abbr = (/"Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"/)

;---Read in temperature and convert to degrees C.
    t       = f->sst
    t@units = "degC"
    t_f   = f_f->sst
    t_f@units = "degC"
    t_n   = f_n->sst
    t_n@units = "degC"

;---Start the graphics
    wks  = gsn_open_wks("png","CNOP_3_29")         ; send graphics to PNG file

    res                     = True
    res@gsnDraw             = False
    res@gsnFrame            = False
    res@mpFillOn            = False            ; no need
    res@mpCenterLonF        = -180.0

    res@mpMaxLatF           = 20.                      ; specify the plot domain
    res@mpMinLatF           = -20.                      ;
    res@mpMinLonF           = 120.                     ;
    res@mpMaxLonF           = 280.

    res@cnLevelSelectionMode= "ManualLevels"   ; manual set levels
    res@cnMinLevelValF      = -8.0
    res@cnMaxLevelValF      = 8.0
    res@cnLevelSpacingF     = 0.4              ; 20 contour levels
    res@cnFillOn            = True             ; color fill plot
    res@cnLinesOn           = False
    res@cnLineLabelsOn      = False
    res@cnInfoLabelOn       = False
    res@cnFillPalette       = "BlueDarkRed18"

    res@lbLabelBarOn        = False            ; turn off individual label bars

    res@gsnStringFontHeightF= 0.02
    res@gsnLeftString       = "SST"
    res@gsnRightString      = t@units

;---Create arrays to hold series of plots
    plots      = new(12, graphic)

    ; do i=0, 8
;---Get data for start and end year of interest
      ; t(i, :, :) = t(i, :, :) - t_f(51 + i, :, :)
      ; print(avg(t(i, 62:129, 79:129)))
;---Create the two start/end year plots and the difference plot
      ; res@gsnCenterString = month_abbr(i)
      ; plots(i) = gsn_csm_contour_map_ce(wks, t(i, :, :), res)
    ; end do

    do i=0, 11
;---Get data for start and end year of interest
      t(i, :, :) = t(i, :, :) - t_n(i + 3, :, :)
      print(avg(t(i, 62:129, 79:129)))
;---Create the two start/end year plots and the difference plot
      res@gsnCenterString = month_abbr(i)
      plots(i) = gsn_csm_contour_map_ce(wks, t(i, :, :), res)
    end do

;---Resources for paneling
    pres                   = True              ; modify the panel plot
    pres@gsnPanelMainString= fname
    pres@gsnFrame          = False             ; don't advance frame yet
    pres@gsnDraw           = False             ; draw later, in maximize mode
    pres@gsnPanelBottom    = 0.33              ; top 2/3 of frame

    pres@gsnPanelLabelBar  = True              ; add common colorbar
    pres@lbOrientation     = "vertical"
    pres@pmLabelBarWidthF  = 0.075             ; make thinner
    pres@pmLabelBarHeightF = 0.40

;
; It is necessary to return the id of the paneled plots,
; so they can "live" for the rest of this script, for
; when we maximize them later.
;
    panelid1 = gsn_panel_return(wks, plots, (/3, 4/), pres)

;---Calculate location for top of difference plots
    bb     = NhlGetBB(panelid1)
    bottom = min(bb(:, 1))
    top    = max(bb(:, 0))
    height = (top-bottom) / 2.     ; Height of one row

;---Panel the diff plots at the bottom
;    delete(pres@gsnPanelMainString)
;    pres@gsnPanelTop       = bottom-0.01    ; lower 1/3 plus some white space
;    pres@gsnPanelBottom    = pres@gsnPanelTop - height

;    pres@pmLabelBarHeightF = 0.20

;    panelid2 = gsn_panel_return(wks,diff_plots,(/1,2/),pres)

;---This will maximize the size of all the paneled stuff.
    maximize_output(wks,True)
end
