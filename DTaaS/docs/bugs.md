# Few issues in the Software

If you find a bug, please
[open an issue](https://github.com/INTO-CPS-Association/DTaaS/issues/new)

## Third-Party Software

The explanation given below corresponds to the bugs you may face
from third party software included in DTaaS.
Known issues are listed below.

### ML Workspace

- the docker container might down a bit after two weeks.
  The only known solution is to restart the docker container.
  You don't need to restart the complete DTaaS platform, restart of
  the docker container of ml-workspace is sufficient.
- the terminal tool doesn't seem to have the ability to refresh itself.
  If there is an issue, the only solution is to close and
  reopen the terminal from "open tools" drop down of notebook
- terminal app does not show at all after some time: terminal always
  comes if it is open from drop-down menu of Jupyter Notebook,
  but not as a direct link.

## Gitlab

- The gilab oauth authorization service does not
  have a way to sign out of a third-party application.
  Even if you sign out of DTaaS, the gitlab still shows user as signed in.
  The next time you click on the sign in button on the DTaaS page,
  user is not shown the login page.
  Instead user is directly taken to the **Library** page.
  So close the brower window after you are done.
  Another way to overcome this limitation is to open your
  gitlab instance (`https://gitlab.foo.com`) and signout from there.
  Thus user needs to sign out of two places, namely DTaaS and gitlab,
  in order to completely exit the DTaaS application.
