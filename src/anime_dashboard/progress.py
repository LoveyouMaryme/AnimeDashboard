



def should_update(platform_ep_number: int, mal_ep_number: int ) -> bool :
        """

        Determine if MAL should be updated by the source progress
        
        Args: 
            platform_ep_number : Number of episodes recorded by the source
            mal_ep_number: Numer of episodes currently recorded by MAL

        Returns:
            True if an update is required, false if not

        Raises:
            ValueError : if a progress value is negative
            
        """
        if platform_ep_number < 0 or mal_ep_number < 0:
            raise ValueError("Ce n'est pas possible que l'épisode soit négatif")
        
        
        return platform_ep_number > mal_ep_number;


