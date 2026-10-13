# CRESCENT-CVM-S3-DATA


Bundles the CRESCENT Community Velocity Model data files and publishes them to the S3 bucket used by the [CVM viewer](https://github.com/cascadiaquakes/CRESCENT-CVM-WEB).

**Used by:** https://cvm.cascadiaquakes.org

---

## Large Files

Due to GitHub file size limits (100 MB), one or more of the files in this repository [are now tracked ](https://docs.github.com/en/repositories/working-with-files/managing-large-files/moving-a-file-in-your-repository-to-git-large-file-storage) using GitHub's LFS (Large File Support).

For a better experience, [install git large file support](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage) before cloning and working with this git repository.

If LFS is already enabled globally in your local git config (via `git lfs install`), then a clone operation will automatically pull down the large blobs.  If you cloned a repo without first having git LFS installed, large objects can later be downloaded with `git lfs fetch`.

---

## Deployment

The CDK app in `infra/cvm-s3-data/` defines the bucket and uploads. The GitHub Actions workflow in `.github/workflows/main.yml` validates it on pull requests to `main` and deploys on pushes to `main`.

---

## Contacts

- **William Marfo**, University of California, Davis: [wmarfo@ucdavis.edu](mailto:wmarfo@ucdavis.edu)
- **Loïc Bachelot**, University of Oregon: [lbachelo@uoregon.edu](mailto:lbachelo@uoregon.edu)

For bugs or questions, please [open an issue](https://github.com/cascadiaquakes/CRESCENT-CVM-S3-DATA/issues).

---

## Acknowledgments

<table>
  <tr>
    <td align="center" valign="middle">
      <img src="https://raw.githubusercontent.com/cascadiaquakes/.github/main/assets/crescent-circle.png" alt="CRESCENT Logo" width="150" />
    </td>
    <td align="center" valign="middle">
      <img src="https://raw.githubusercontent.com/cascadiaquakes/.github/main/assets/nsf-logo.png" alt="NSF Logo" width="450" />
    </td>
  </tr>
</table>

This project is supported by the National Science Foundation through the Cascadia Region Earthquake Science Center (CRESCENT), Cooperative Agreement EAR-2225286.
