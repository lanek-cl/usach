class Config:
    """
    A configuration class containing default settings for various parameters.

    Attributes
    ----------
    Default : class
        Nested class containing default boolean flags for advanced options, sound, and triggers.

    Trigger : class
        Nested class defining the default, minimum, maximum, and step values for the trigger parameter.

    Tone : class
        Nested class defining the default, minimum, maximum, and step values for the tone parameter, along with the sample rate.

    Duration : class
        Nested class defining the default, minimum, maximum, and step values for the duration parameter.
    """

    class Default:
        """
        Default settings for basic options.

        Attributes
        ----------
        avanzado : bool
            A flag to indicate whether advanced mode is enabled. Default is False.
        no_sound : bool
            A flag to disable sound. Default is False.
        no_trigger : bool
            A flag to disable triggers. Default is False.
        """

        avanzado = False
        no_sound = False
        no_trigger = False

    class Trigger:
        """
        Configuration for trigger settings.

        Attributes
        ----------
        default : int
            The default trigger value. Default is 100.
        min : int
            The minimum trigger value. Default is 100.
        max : int
            The maximum trigger value. Default is 1000.
        step : int
            The step size for the trigger value. Default is 100.
        """

        default = 100
        min = 100
        max = 1000
        step = 100

    class Tone:
        """
        Configuration for tone settings.

        Attributes
        ----------
        default : int
            The default tone frequency in Hz. Default is 1000 Hz.
        min : int
            The minimum tone frequency in Hz. Default is 500 Hz.
        max : int
            The maximum tone frequency in Hz. Default is 5000 Hz.
        step : int
            The step size for tone frequency in Hz. Default is 500 Hz.
        sample_rate : int
            The sample rate in Hz for the tone. Default is 44100 Hz.
        """

        default = 1000
        min = 500
        max = 5000
        step = 500
        sample_rate = 44100

    class Duration:
        """
        Configuration for duration settings.

        Attributes
        ----------
        default : int
            The default duration in seconds. Default is 2 seconds.
        min : int
            The minimum duration in seconds. Default is 1 second.
        max : int
            The maximum duration in seconds. Default is 5 seconds.
        step : int
            The step size for duration in seconds. Default is 1 second.
        """

        default = 2
        min = 1
        max = 5
        step = 1
