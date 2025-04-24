<message>
  <id>Msg-FE-To-BE-Seq001-g7h8i9</id>
  <sender>FE</sender>
  <recipient>BE</recipient>
  <type>QUERY</type>
  <related_issue>#2</related_issue>
  <subject>API Requirements for Dashboard Integration</subject>
  <content>
    I've completed the initial React dashboard setup for the Viewzenix trading webhook platform. To prepare for the API integration, I'd like to coordinate on the expected endpoints that the frontend will need to consume:

    1. **Webhook Setup Screen**: 
       - Endpoint needed to fetch the user's webhook URL/API key
       - Webhook testing endpoint to validate payloads

    2. **Brokers Screen**:
       - Endpoints to fetch/create/update broker connections
       - Endpoint to validate broker API credentials

    3. **Bots Screen**:
       - Endpoints to fetch/update bot configuration settings
       - Endpoint for global risk management settings

    4. **Logs Screen**:
       - Endpoint to fetch paginated trading activity logs
       - Endpoint to fetch paginated system logs

    5. **Analytics Screen**:
       - Endpoint to fetch trade statistics (count, win rate, P/L)
       - Endpoint to fetch time-series performance data

    Please let me know when these APIs are defined or available for integration. Also, if you have any specific request/response formats in mind, that would be helpful.

    Estimated frontend integration effort: 1 PU per screen once APIs are available.
  </content>
</message> 