# Grafana

We will take advantage of the Grafana server side rendering feature that can render any panel on the server. To verify that this feature works try the *Direct link rendered image* in the panel share dialog. If you do not get an image when opening this link read [here](https://grafana.com/docs/administration/image_rendering/) how to configure this feature.

<img src="../images/grafa_1.png" width="60%" hight="60%">

Create API key ([how to](https://grafana.com/docs/http_api/auth/)) or get cookie from your browser session.

Here is the example how to copy cookie from Chrome:
- Log in to Grafana
- Go to any Grafana panel *Direct link rendered image*
- Hit F12 to open the developer console (macOS: Cmd+Opt+J)
- Look at the Network tab
- Refresh the page
Right click the request in the Network tab, and select "Copy as cURL"

This will give you the curl command with cookie.





