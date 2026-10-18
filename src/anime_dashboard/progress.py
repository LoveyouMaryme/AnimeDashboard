from dataclasses import dataclass

@dataclass
class Progress:
    platform_ep_number: int
    mal_ep_number: int




    def should_update(self) -> bool :
        """

        Determine if MAL should be updated by the source progress
        
        Args: 
            source_ep_number : Number of episodes recorded by the source
            mal_ep_number: Numer of episodes currently recorded by MAL

        Returns:
            True if an update is required, false if not

        Raises:
            ValueError : if a progress value is negative
            
        """

        if self.platform_ep_number < 0 or self.mal_ep_number < 0:
            raise ValueError("Ce n'est pas possible que l'épisode soit négatif")

        
        return self.platform_ep_number > self.mal_ep_number;


