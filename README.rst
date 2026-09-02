
radio-astro-tools tutorials
---------------------------

Jupyter notebook tutorials on a variety of topics using
the radio-astro-tools packages, including a translation guide
for CASA users.

Visit the `tutorial page <https://radio-astro-tools.github.io/tutorials/>`_
to access the rendered notebooks and helpful links for interactive
using with `Binder <https://mybinder.org/>`_.

Development
-----------

Notebooks are kept free of cell outputs on ``master`` so diffs stay
reviewable. This is enforced by a ``pre-commit`` hook (`nbstripout
<https://github.com/kynan/nbstripout>`_) plus a CI check that fails if a
notebook with outputs is pushed. To set up the hook locally::

    pip install pre-commit nbstripout
    pre-commit install
