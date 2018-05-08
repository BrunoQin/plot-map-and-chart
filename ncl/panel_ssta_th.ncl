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
    fname = "../9_15_ocean.nc"
    f     = addfile(fname,"r")
    fname_ave = "/BIGDATA1/iocas_mmu_2/GFDL-CM2p1/output/00610101.ocean_month.nc"
    f_ave     = addfile(fname_ave,"r")

;---Convert "time" to an ntim x 6 array of year,mon,day,hour,min,sec
;    newtime = cd_calendar(f->time,0)
;    years   = newtime(:,0)
;    months  = newtime(:,1)

    newtime = cd_calendar(f->time,0)
    months  = newtime(:,1)
    start_months = (/1,2,3,4,5,6/)
    end_months   = (/7,8,9,10,11,12/)
    nmonths      = dimsizes(start_months)
    month_abbr = (/"","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep", \
                    "Oct","Nov","Dec"/)
;---Indicate start and end years of interest. Best to only do 1 or 2 here
;    month      = 1                  ; January
;    smonth     = "Jan"
;    start_years = (/1951,1961/)
;    end_years   = (/1991,2001/)
;    nyears      = dimsizes(start_years)

;---Read in temperature and convert to degrees C.
    t       = f->sst
    t@units = "degC"
    t_ave   = f_ave->sst
    t_ave@units = "degC"
;---Start the graphics
    wks  = gsn_open_wks("png","panel6")         ; send graphics to PNG file

    res                     = True
    res@gsnDraw             = False
    res@gsnFrame            = False
    res@mpFillOn            = False            ; no need
    res@mpCenterLonF        = -180.0

    res@mpMaxLatF    = 20.                      ; specify the plot domain
    res@mpMinLatF    = -20.                      ;
    res@mpMinLonF    = 120.                     ;
    res@mpMaxLonF    = 280.

    res@cnLevelSelectionMode= "ManualLevels"   ; manual set levels
    res@cnMinLevelValF      = -4.0
    res@cnMaxLevelValF      = 4.0
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
    plots      = new(2*nmonths,graphic)

    do i=0, nmonths-1
;---Get data for start and end year of interest
;     sy = ind(years.eq.start_years(i).and.months.eq.month)
;     ey = ind(years.eq.end_years(i)  .and.months.eq.month)

;      diff = t(sy,:,:)                ; trick to copy  metadata
;      diff = t(ey,:,:) - t(sy,:,:)    ; overwrite with diff values

;      diff@long_name = end_years(i) + "-" + start_years(i) + \
;                       " TS field differences"
      sy = ind(months.eq.start_months(i))
      ey = ind(months.eq.end_months(i))
      print(sy)
      print(ey)
;---Debug prints
      ; print("========================================")
      t(i,:,:) = t(i,:,:)-t_ave(i+24,:,:)
      t(i+6,:,:) = t(i+6,:,:)-t_ave(i+6+24,:,:)
      ; printMinMax(t(sy,:,:),0)
      ; printMinMax(t(ey,:,:),0)
;      printMinMax(diff,0)

;---Create the two start/end year plots and the difference plot
     ; sy = ind(months.eq.start_months(i))
     ; ey = ind(months.eq.end_months(i))
      res@gsnCenterString = month_abbr(start_months(i))
      plots(i*2) = gsn_csm_contour_map_ce(wks, t(i,:,:), res)

      res@gsnCenterString = month_abbr(end_months(i))
      plots(i*2+1) = gsn_csm_contour_map_ce(wks,t(i+6,:,:), res)

;      dres@gsnCenterString = "Difference: " + smonth + " " + \
;                             end_years(i) + "-" + start_years(i)
;      diff_plots(i) = gsn_csm_contour_map_ce(wks, diff ,dres)
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
    panelid1 = gsn_panel_return(wks,plots,(/nmonths,2/),pres)

;---Calculate location for top of difference plots
    bb     = NhlGetBB(panelid1)
    bottom = min(bb(:,1))
    top    = max(bb(:,0))
    height = (top-bottom)/2.     ; Height of one row

;---Panel the diff plots at the bottom
;    delete(pres@gsnPanelMainString)
;    pres@gsnPanelTop       = bottom-0.01    ; lower 1/3 plus some white space
;    pres@gsnPanelBottom    = pres@gsnPanelTop - height

;    pres@pmLabelBarHeightF = 0.20

;    panelid2 = gsn_panel_return(wks,diff_plots,(/1,2/),pres)

;---This will maximize the size of all the paneled stuff.
    maximize_output(wks,True)
end
