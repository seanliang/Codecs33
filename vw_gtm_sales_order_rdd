CREATE OR REPLACE VIEW ldlads.vw_gtm_sales_order_rdd
AS
  SELECT sales_document_number
       , sales_document_item
       , REGEXP_REPLACE(SUBSTR(schedule_line_delivery_date, 1, 10), '-', '') AS requested_delivery_date
       , record_creation_date
  FROM
    ldldws.fact_sales_schedule_line
  WHERE schedule_line_number = '1'
    AND pt_sellin_month >= DATE_FORMAT(ADD_MONTHS(DATE_ADD(CURRENT_TIMESTAMP, -1), -2), 'yyyy-MM')
;
