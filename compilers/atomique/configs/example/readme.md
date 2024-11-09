# Example Usage of Config Files.
This folder contains example usage of configuration files, utilizing torchpack to manage these configurations. The directory structure is organized as follows:    

```
example
├── arb
│   ├── default.yml
│   ├── fpqac.yml
├── default.yml
```

To run the example, execute the following command:
```bash
python run.py configs/example/arb/fpqac.yml
```
The `fpqac.yml` file inherits settings from `default.yml`. In the event of any conflicts between the two, settings in `fpqac.yml` will override those in the default.yml file within the same directory, and subsequently, this `default.yml` will override the `default.yml` file in the parent directory.

Key Features of the Configuration Files:
+ Inheritance: Allows for inheriting settings from a parent configuration file while providing the option to override them.
+ Parallel Execution: Supports running multiple configuration files simultaneously.
+ Combination of Parameters: Enables customization of parameter combinations to facilitate multiple experiments within a single configuration file.

For detailed information on all parameters and their applications, please refer to the three files located under the example directory.
