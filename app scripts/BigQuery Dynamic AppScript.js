// Zip2Utility - Dynamic - Runs a BigQuery query, sending Zip (from active sheet) and returning Utility Info.
function zip2UtilityDynamic() {
  var projectId = 'seinergydbv2';
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = spreadsheet.getSheetByName("Dashboard");
  var zip = sheet.getRange('A2').getValues();
  var request = {
    query: 'SELECT * FROM [seinergydbv2:LookupTables.zip2EIAID] WHERE zip=' + zip
    };
  var queryResults = BigQuery.Jobs.query(request, projectId);
  var jobId = queryResults.jobReference.jobId;

  // Check on status of the Query Job.
  var sleepTimeMs = 500;
  while (!queryResults.jobComplete) {
    Utilities.sleep(sleepTimeMs);
    sleepTimeMs *= 2;
    queryResults = BigQuery.Jobs.getQueryResults(projectId, jobId);
  }

  // Get all the rows of results.
  var rows = queryResults.rows;
  while (queryResults.pageToken) {
    queryResults = BigQuery.Jobs.getQueryResults(projectId, jobId, {
      pageToken: queryResults.pageToken
    });
    rows = rows.concat(queryResults.rows);
  }

  if (rows) {
  //  var spreadsheet = SpreadsheetApp.create('BiqQuery Results');
    var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    var sheetResults = spreadsheet.getSheetByName("zip2Utility_results");

    // Append the headers.
    // var headers = queryResults.schema.fields.map(function(field) {
    //  return field.name;
    // });
    // sheetResults.appendRow(headers);

    // Append the results.
    var data = new Array(rows.length);
    for (var i = 0; i < rows.length; i++) {
      var cols = rows[i].f;
      data[i] = new Array(cols.length);
      for (var j = 0; j < cols.length; j++) {
        data[i][j] = cols[j].v;
      }
    }
    sheetResults.getRange(2, 1, rows.length, 10).setValues(data);
    

  Logger.log('Results spreadsheet created: %s',
       spreadsheet.getUrl());
  } else {
    Logger.log('No rows returned.');
  }
}
// [END apps_script_bigquery_run_query]

/***************************************/
// eiaid2Estimate - Dynamic - Runs a BigQuery query, sending eiaid_state and returning quantative info for quick estimate.
function eiaid2Estimate() {
   var projectId = 'seinergydbv2';
   var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
   var sheet = spreadsheet.getSheetByName("EIAID_state2estimateInput");
   var eiaidstate = sheet.getRange('A2').getValues();
  var request = {
    query: 'SELECT * FROM [seinergydbv2:LookupTables.slimEstimateDetails] WHERE eiaidstate="' + eiaidstate + '\"' //PROBLEM HERE
    };
  var queryResults = BigQuery.Jobs.query(request, projectId);
  var jobId = queryResults.jobReference.jobId;

  // Check on status of the Query Job.
  var sleepTimeMs = 500;
  while (!queryResults.jobComplete) {
    Utilities.sleep(sleepTimeMs);
    sleepTimeMs *= 2;
    queryResults = BigQuery.Jobs.getQueryResults(projectId, jobId);
  }

  // Get all the rows of results.
  var rows = queryResults.rows;
  while (queryResults.pageToken) {
    queryResults = BigQuery.Jobs.getQueryResults(projectId, jobId, {
      pageToken: queryResults.pageToken
    });
    rows = rows.concat(queryResults.rows);
  }

  if (rows) {
  //  var spreadsheet = SpreadsheetApp.create('BiqQuery Results');
    var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    var sheetResults = spreadsheet.getSheetByName("eiaid2Estimate_results");

   // Append the headers.
   // var headers = queryResults.schema.fields.map(function(field) {
   // return field.name;
   // });
   // sheetResults.appendRow(headers);

    // Append the results.
    var data = new Array(rows.length);
    for (var i = 0; i < rows.length; i++) {
      var cols = rows[i].f;
      data[i] = new Array(cols.length);
      for (var j = 0; j < cols.length; j++) {
        data[i][j] = cols[j].v;
      }
    }
    sheetResults.getRange(2, 1, rows.length, 9).setValues(data);
    

  Logger.log('Results spreadsheet created: %s',
       spreadsheet.getUrl());
  } else {
    Logger.log('No rows returned.');
  }
}
// [END apps_script_bigquery_run_query]

